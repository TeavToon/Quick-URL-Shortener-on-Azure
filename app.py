from fastapi import FastAPI, HTTPException, Depends, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import secrets, validators, os
from sqlalchemy.orm import Session
from database import SessionLocal, URLModel, engine, Base

app = FastAPI()

# สร้างตารางเมื่อแอปเริ่มทำงาน (ถ้ายังไม่มี)
Base.metadata.create_all(bind=engine)

# ตั้งค่าให้ FastAPI รู้จักโฟลเดอร์ templates
templates = Jinja2Templates(directory="templates")

# 1. เพิ่ม Route สำหรับแสดงหน้าแรก (หน้าบ้าน)
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Dependency สำหรับดึง DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten")
def create_short_url(full_url: str, db: Session = Depends(get_db)):
    if not validators.url(full_url):
        raise HTTPException(status_code=400, detail="URL ไม่ถูกต้อง")
    
    short_code = secrets.token_urlsafe(5)
    
    # บันทึกลง Database
    db_url = URLModel(short_code=short_code, full_url=full_url)
    db.add(db_url)
    db.commit()
    
    # ดึง Domain จาก Environment (เช่น https://my-app.azurewebsites.net)
    base_url = os.getenv("BASE_URL", f"https://{os.getenv('WEBSITE_HOSTNAME')}")
    return {"short_url": f"{base_url}/{short_code}"}

@app.get("/{short_code}")
def redirect_to_full(short_code: str, db: Session = Depends(get_db)):
    db_url = db.query(URLModel).filter(URLModel.short_code == short_code).first()
    
    if db_url:
        return RedirectResponse(url=db_url.full_url)
    raise HTTPException(status_code=404, detail="ไม่พบลิงก์นี้")