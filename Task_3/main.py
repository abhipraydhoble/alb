from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch

app = FastAPI()

# Load the model and tokenizer
model_name = "distilbert-base-uncased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

class ParagraphInput(BaseModel):
    paragraph: str

@app.post("/generate-questions")
def generate_questions(input: ParagraphInput):
    if not input.paragraph:
        raise HTTPException(status_code=400, detail="Input paragraph cannot be empty")

    # Tokenize the input paragraph
    inputs = tokenizer.encode_plus(input.paragraph, add_special_tokens=True, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    # Generate questions and answers (this part needs improvement for real use)
    start_scores, end_scores = model(**inputs, return_dict=False)
    all_tokens = tokenizer.convert_ids_to_tokens(input_ids)
    answer = ' '.join(all_tokens[torch.argmax(start_scores): torch.argmax(end_scores)+1])

    questions = ["What is the main topic?"]
    answers = [answer]

    return {"questions": questions, "answers": answers}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
