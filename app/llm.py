import ollama 

MODEL = "qwen2.5:7b"

def ask(promt: str, system: str = "Ты полезный ассистент.")-> str:
    """Отправляет вопрос модели и возвращает текст ответа."""
    response = ollama.chat(
        model=MODEL,
        messages=[
            {"role": "system", "content": system},#Отправляем роль и правила поведения по которым потом зададим роли агентов
            {"role": "user", "content": promt,} # сама задача(промт)
        ],
    )
    
    return response["message"]["content"]