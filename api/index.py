@app.route("/api/TitleData", methods=["POST", "GET"])
def title_data():
    response = requests.post(
        url=f"https://{settings.TitleId}.playfabapi.com/Server/GetTitleData",
        headers=settings.get_auth_headers()
    )

    if response.status_code == 200:
        return jsonify(response.json().get("data").get("Data"))
    else:
        return jsonify({}), response.status_code
