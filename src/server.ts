import "dotenv/config";
import express, { Application, Request, Response } from "express";
import http from "http";
import OpenAI from "openai";

const app: Application = express();

const server = http.createServer(app);

const apiKey = process.env.OPENAI_API_KEY;

if (!apiKey) {
  console.error("OPENAI_API_KEY environment variable is missing");
  process.exit(1);
}

const openAI = async () => {
  const openai = new OpenAI({ apiKey });
  const completion = await openai.chat.completions.create({
    messages: [{ role: "system", content: "You are a helpful assistant." }],
    model: "gpt-4",
  });
  console.log(completion.choices[0]);
  return completion;
};

app.get("/", async (req: Request, res: Response) => {
  try {
    const response = await openAI();
    return res.status(200).send({ response });
  } catch (error) {
    return res.status(500).send(error);
  }
});

server.listen(8000, () => console.log(`Server is listening on port 8000!`));
