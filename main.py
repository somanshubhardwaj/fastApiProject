from fastapi import FastAPI

app = FastAPI()

a = [{"id": 1, "title": "title1", "body": "body1", "subcode": "PH", "subname": "Engineering PHY"},
     {"id": 2, "title": "title2", "body": "body2", "subcode": "PH", "subname": "Engineering PHY"},
     {"id": 3, "title": "title3", "body": "body3", "subcode": "PH", "subname": "Engineering PHY"},
     {"id": 4, "title": "title4", "body": "body4", "subcode": "PH", "subname": "Engineering PHY"}
     ]


@app.get("/posts")
async def root():
    return a


@app.get("posts/{i}")
async def root(i: int):
    return a[i]


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/string/upper/{name}")
async def uppercase(name: str):
    return {"string": f"{name.upper()}"}


@app.get("/string/lower/{name}")
async def lowercase(name: str):
    return {"string": f"{name.lower()}"}


@app.get("/string/length/{name}")
async def length(name: str):
    return {"length": f"{len(name)}"}


@app.get("/string/reverse/{name}")
async def reverse(name: str):
    return {"reverse": f"{name[::-1]}"}


@app.get("/string/palindrome/{name}")
async def palindrome(name: str):
    if name == name[::-1]:
        return {"palindrome": True}
    else:
        return {"palindrome": False}


@app.get("/string/word-count/{name}")
async def word_count(name: str):
    return {"word-count": f"{len(name.split())}"}


@app.get("/string/word-count/{name}/{word}")
async def word_count(name: str, word: str):
    return {"word-count": f"{name.count(word)}"}
