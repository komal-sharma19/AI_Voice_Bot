import google.generativeai as genai
import os

# Make sure to set your API key as an environment variable
# or replace "YOUR_API_KEY" with your actual key for this test.
genai.configure(api_key="AIzaSyCh9A_m7pYfCZwYfxV4bQ1iPIVmYKc0_pU")

print("Available models that support 'generateContent':")

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    print(m.name)