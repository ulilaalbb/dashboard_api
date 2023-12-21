from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from pydantic import BaseModel





def prediction_data(test_input):
    # Load the trained model, vectorizer, and label encoder
    with open('bobot_model.pkl', 'rb') as file:
        saved_objects = pickle.load(file)
    loaded_model =saved_objects['model']
    loaded_vectorizer = saved_objects['vectorizer']
    loaded_label_encoder = saved_objects['label_encoder']

    print(test_input)
    norm_input = loaded_vectorizer.transform([test_input])
    prediction = loaded_model.predict(norm_input)
    prediction = loaded_label_encoder.inverse_transform(prediction)
    return prediction[0]







# # SQLAlchemy Database Configuration
# DATABASE_URL = "mysql+mysqlconnector://root@localhost/dashboard_kpi"
# engine = create_engine(DATABASE_URL)

# Base = declarative_base()

# class TestCase(Base):
#     __tablename__ = "test_case"  # Replace with your actual table name

#     id = Column(Integer, primary_key=True, index=True)
#     test_case_id = Column(String, index=True)
#     topic = Column(String, index=True)
#     description = Column(String, index=True)
#     test_plan = Column(String)
#     weight = Column(Integer)

# Base.metadata.create_all(bind=engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Pydantic model for form data
# class TestCaseInput(BaseModel):
#     test_case_id: str
#     topic: str
#     description: str
#     test_plan: str

# # FastAPI route to handle predictions
# @app.post("/test_case/store")
# async def predict(test_case_input: TestCaseInput):
#     # Preprocess the input using the loaded vectorizer
#     description_tfidf = loaded_vectorizer.transform([test_case_input.description])

#     # Make predictions using the loaded classifier
#     predicted_label = loaded_model.predict(description_tfidf)

#     # Decode the predicted label using the loaded label encoder
#     predicted_weight = int(loaded_label_encoder.inverse_transform(predicted_label)[0])

#     # Store the data in the MySQL table
#     db = SessionLocal()
#     db_test_case = TestCase(**test_case_input.dict(), weight=predicted_weight)
#     db.add(db_test_case)
#     db.commit()
#     db.refresh(db_test_case)
#     db.close()

#     return {"predicted_weight": predicted_weight}

