FROM python

WORKDIR /pythonsoorya

COPY . /pythonsoorya/

EXPOSE 8501

RUN pip install -r requirements.txt

CMD streamlit run server.py