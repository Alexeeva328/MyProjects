import json
blackjack_hand = (8, "Q")
encoded_hand = json.dumps(blackjack_hand)
decoded_hand = json.loads(encoded_hand)

#print(blackjack_hand == decoded_hand) # False
#print(type(blackjack_hand)) # <class 'tuple'>
#print(type(decoded_hand)) # <class 'list'>
#print(blackjack_hand == tuple(decoded_hand)) # True

body={"method":"get",
      "params":["Id","Name"]
      }

#кодирование тела запроса в JSON
jsonBody=json.dumps(body,ensure_ascii=False).encode('utf8')

#js=json.loads(jsonBody)
js=json.dump(jsonBody)
print("jsonBody",jsonBody)
print("js",js)
