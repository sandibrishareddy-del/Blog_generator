!pip -q install google-genai gradio
from google import genai
import gradio as gr
client = genai.Client(api_key="YOUR_API_KEY")
def generate_blog(topic, audience, tone, words):
  prompt = f"""
  Write a {words}-word blog.
  Topic: {topic}
  Audience: {audience}
  Tone: {tone}
  Include:
  - Title
  - Introduction
  - Key points
  - Examples
  - Disadvantages
  - Conclusion
  """
  response = client.models.generate_content(
      model="gemini-2.5-flash",
      contents=prompt
  )
  return response.text
demo = gr.Interface(
    fn=generate_blog,
    inputs=[
        gr.Textbox(label="Topic"),
        gr.Textbox(label="Audience"),
        gr.Dropdown(
            ["Professional","Casual","Funny","Technical","Inspirational"],
            label="Tone"
        ),
        gr.Slider(200,1000,value=500,label="Word Count")
    ],
    outputs="markdown",
    title="AI Blog Generator (Gemini)"
)
demo.launch()
