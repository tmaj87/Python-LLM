import chromadb
import ollama
from chromadb.api.models.Collection import Collection

DOCUMENTS = [
    "I am a passionate software developer with over 20 years of experience, dedicated to creating and maintaining impactful solutions. My approach is deeply hands-on and proactive, always focused on identifying opportunities for improvement.",
    "My fascination with technology began with the development of ARPANET, inspiring me to explore dynamic, widely accessible web pages. Over time, this passion evolved into a career in web development, branching into areas like task automation scripting and early explorations in ethical hacking.",
    "My professional journey began with JavaScript, PHP, and SQL—considered robust tools of their time. Recognizing the need for enterprise-grade solutions, I transitioned to Java, which introduced me to core concepts like design patterns, test-driven development, and clean, maintainable code structures. Collaborative environments taught me the value of teamwork in delivering exceptional software.",
    "As my career progressed, I sought roles that provided greater involvement in product development. I led features from initial story definition through production release and ongoing monitoring, gaining experience in team leadership and mentorship along the way. Recently, I’ve expanded my technical repertoire to include Go, Ruby, and Python, with a consistent focus on full-stack development through React.",
    "IT security is one of my strongest passions. I find it rewarding to analyze and strengthen software against vulnerabilities, understanding how development choices can expose systems to risks like reverse-engineering or unauthorized modification. This mindset informs my approach to designing secure, resilient solutions.",
    "Another area of deep interest is artificial intelligence, which I believe is reshaping the world. This curiosity has driven me to explore Rust, further diversifying my technical skill set.",
]
CLIENT = chromadb.Client()


def response(prompt: str):
    return ollama.embeddings(prompt=prompt, model="mxbai-embed-large")


def store(collection: Collection):
    for key, val in enumerate(DOCUMENTS):
        embedding = response(val).get("embedding", "")
        collection.add(ids=[str(key)], embeddings=[embedding], documents=[val])


def retrieve(collection: Collection, prompt: str):
    embedding = response(prompt).get("embedding", "")
    results = collection.query(query_embeddings=[embedding], n_results=3)
    return results["documents"][0]


if __name__ == "__main__":
    documents = CLIENT.create_collection(name="tomaj")
    store(documents)
    prompt = "What languages does he know?"
    resp = retrieve(documents, prompt)
    output = ollama.generate(
        model="llama3.2",
        prompt=f"Using this data: {resp}. Respond to this prompt: {prompt}",
    )
    print(output.response)
