# What is Generative AI?
- **Generative AI (GenAI)** refers to AI systems that can **create new content** (not just analyze existing data).  
- The generated content can include:  
  - **Text** (e.g., chatbots, code generation)  
  - **Images** (e.g., AI art, image editing)  
  - **Audio & Music** (e.g., voice synthesis, music composition)  
  - **Video** (e.g., deepfakes, video generation)  
- Unlike traditional AI (which focuses on _classification or prediction_), **GenAI produces original outputs** that resemble human-created data.  

---
##  Example Text Generation (JS/TS)
- Using **OpenAI’s** API to generate text:  
```ts
import OpenAI from "openai";  
// Imports the official OpenAI SDK

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});  
// Creates a client instance with your API key

const response = await client.chat.completions.create({
  model: "gpt-4o-mini",
  messages: [{ role: "user", content: "Write a short poem about coffee." }],
});  
// Sends a request to the Chat Completions API with model + messages

console.log(response.choices[0].message.content);  
// Logs the model’s generated response
```

---
