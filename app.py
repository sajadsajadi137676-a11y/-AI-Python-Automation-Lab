
import pypdf
import openai
import pandas as pd

# ۱. خواندن متن خام از فایل پی‌دی‌اف کانادایی
def read_pdf(file_path):
    with open(file_path, "rb") as file:
        reader = pypdf.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

# ۲. ارسال متن به هوش مصنوعی برای تفکیک دقیق داده‌ها
def extract_engineers_data(raw_text):
  openai.api_key = "sk-your-key-here"

    
    prompt = f"""
    Extract the Name, Title, Degree, and Skills of all engineers from the text below. 
    Output ONLY raw text with each engineer on a new line and metrics separated by commas, 
    with no brackets, curly braces, markdown, or extra words.
    
    Data:
    {raw_text}
    """
    
    response = openai.chat.completions.create(
        model="gpt-4o-mini", # مدل پرسرعت و دقیق
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

# ۳. تبدیل خروجی متنی به فایل اکسل منظم
def save_to_excel(ai_output, output_excel_path):
    lines = ai_output.strip().split("\n")
    data_list = []
    
    for line in lines:
        if line.strip():
            # جدا کردن بخش‌ها بر اساس ویرگول
            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 4:
                data_list.append({
                    "Name": parts[0],
                    "Title": parts[1],
                    "Degree": parts[2],
                    "Skills": parts[3]
                })
    
    # ساخت دیتافریم با کتابخانه پانداس و خروجی اکسل
    df = pd.DataFrame(data_list)
    df.to_excel(output_excel_path, index=False)
    print(f"🎉 Success! Excel created at: {output_excel_path}")

# مسیر فایل‌ها و اجرای نهایی خط تولید پایتون
pdf_path = "data.pdf"
excel_path = "Canadian_Engineers_Output.xlsx"

try:
    print("⏳ Reading PDF...")
    pdf_text = read_pdf(pdf_path)
    
    print("🧠 Processing with AI...")
    ai_result = extract_engineers_data(pdf_text)
    
    print("📊 Generating Excel file...")
    save_to_excel(ai_result, excel_path)
except Exception as e:
    print(f"❌ Error occurred: {e}")
