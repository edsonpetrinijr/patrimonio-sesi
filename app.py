from flask import Flask, request
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["POST"])
def home():
    productCode = request.json["code"]

    productList = pd.read_csv("./product.csv", on_bad_lines="skip", sep=";")

    product = productList[productList.apply(lambda row: row.astype(str).str.contains(productCode).any(), axis=1)].iloc[0]

    localList = pd.read_csv("./local.csv", on_bad_lines="skip", sep=";")

    room = localList[localList.apply(lambda row: row.astype(str).str.contains(str(product["LOCAL"])).any(), axis=1)].iloc[0]["DENOMINAÇÃO"]

    return {
        "DENOMINAÇÃO": productCode,
        "PATRIMÔNIO": product["DENOMINAÇÃO"],
        "LOCAL": room
    }

if __name__ == "__main__":
    app.run("0.0.0.0")
