
import os, pypdf, openai, pandas as pd
from fastapi import FastAPI
from fastapi.responses import FileResponse
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
app = FastAPI()

@app.get("/process-engineers")
def process_pdf_to_excel():
    try:
        with open("data.pdf", "rb") as f:
            pdf_text = "".join([p.extract_text() for p in pypdf.PdfReader(f).pages])
        prompt = f"Extract Name, Title, Degree, Skills. Format: Name, Title, Degree, Skills. Output ONLY raw text with each on a new line, split by commas:\n{pdf_text}"
        res = openai.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": prompt}])
        data_list = []
        for line in res.choices.message.content.strip().split("\n"):
            if line.strip() and len(line.split(",")) >= 4:
                parts = [p.strip() for p in line.split(",")]
                data_list.append({"Name": parts, "Title": parts, "Degree": parts, "Skills": parts})
        pd.DataFrame(data_list).to_excel("Canadian_Engineers_Output.xlsx", index=False)
        return FileResponse("Canadian_Engineers_Output.xlsx", filename="Canadian_Engineers_Output.xlsx")
    except Exception as e:
        return {"status": "error", "message": str(e)}
