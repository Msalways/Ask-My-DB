
import os
from askdb import AskDB
from askdb.llm.openai_provider import OpenAIProvider
from dotenv import load_dotenv

load_dotenv()


if __name__ == "__main__":
    llm = OpenAIProvider(api_key=os.getenv("API_URL"),base_url="https://openrouter.ai/api/v1", model="meta-llama/llama-4-maverick:free")
    askDb = AskDB(db_url="sqlite:///IMDB.db",llm=llm)
    query,result = askDb.ask("get the movies on action genre with rating more than 5 sort it high to low")
    
    print(query,result)