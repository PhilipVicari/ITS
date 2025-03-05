echo '{
    "contents":[
    {
        "parts":[
            {"text": "What is this picture?"},
            {
                "inline_data": {
                    "mime-type": "image/jpeg",
                    "data": "'$(base64 "Immagine scaricata")'"

                }
            }
        ]
    }
    ]
}'>request.json