from google import genai
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
import re
import os

load_dotenv()
console = Console()

class GeminiClient:
    """
    A client to interact with the Gemini API using the latest google-genai SDK.
    Provides medical symptom analysis with rich, formatted output.
    """

    def __init__(self, model_name: str = 'gemini-2.0-flash'):
        api_key = os.getenv('GEMINI_API_KEY') or os.getenv('GOOGLE_API_KEY')

        if not api_key:
            raise ValueError(
                "API key not found. Please set GEMINI_API_KEY or GOOGLE_API_KEY "
                "in your environment variables or .env file"
            )

        try:
            self.client = genai.Client(api_key=api_key)
            self.model_name = model_name
        except Exception as e:
            raise ConnectionError(f"Failed to initialize Gemini client: {str(e)}")

    def analyze_symptoms(self, symptoms: str) -> str:
        """Analyze medical symptoms and print formatted response."""
        if not symptoms.strip():
            console.print("[red]Error:[/red] Please provide symptoms to analyze.")
            return None

        prompt = self._create_medical_prompt(symptoms)

        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            result = response.text.strip()

            # Convert markdown bold (**) to rich bold ([bold][/bold])
            clean_result = re.sub(r'\*\*(.*?)\*\*', r'[bold]\1[/bold]', result)

            self._display_formatted_output(symptoms, clean_result)
            return clean_result

        except Exception as e:
            console.print(f"[red]Error analyzing symptoms:[/red] {e}")
            return None

    def _create_medical_prompt(self, symptoms: str) -> str:
        """Create a structured prompt for medical symptom analysis."""
        return f"""
Analyze the following symptoms and provide a structured response:

SYMPTOMS PROVIDED:
{symptoms}

Please structure your response as follows:

POSSIBLE CONDITIONS (list 2-4 most likely):
- [Condition name]: [Brief explanation]
- [Condition name]: [Brief explanation]

RECOMMENDED NEXT STEPS:
- [Step 1]
- [Step 2]
- [Step 3]

URGENCY LEVEL:
[Low/Medium/High]

IMPORTANT MEDICAL DISCLAIMERS:
- This analysis is for informational purposes only.
- Consult a qualified healthcare provider for diagnosis.
- Seek emergency help for severe symptoms.
- Individual cases vary; professional evaluation is essential.
"""

    def _display_formatted_output(self, symptoms: str, result: str):
        """Display structured and colored output."""
        console.print(Panel.fit("[bold cyan]🤖 Gemini Medical Symptom Analysis[/bold cyan]", style="bold green"))
        console.print(f"[bold yellow]🩺 Symptoms Provided:[/bold yellow] [white]{symptoms}[/white]\n")
        console.rule("[bold magenta]Analysis[/bold magenta]")
        console.print(result, markup=True)
        console.rule("[bold red]End of Report[/bold red]")

if __name__ == "__main__":
    try:
        client = GeminiClient()
        symptoms = "I have fever since 2 days it was 101 on 1st day and 103 on 2nd"
        client.analyze_symptoms(symptoms)
    except Exception as e:
        console.print(f"[red]Failed to initialize client: {e}[/red]")
