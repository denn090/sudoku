Grundlagen
==========

In diesem Kapitel werden die grundlegenden Konzepte großer Sprachmodelle sowie die im Projekt verwendeten KI-Modelle und Vergleichsmethoden erläutert.
Zunächst wird die Allgemeine Funktionsweise großer Sprachmodelle (LLMs) beschrieben. 
Anschließend erfolgt eine Vorstellung der im Projekt verwendeten Modelle mit Angaben zu Herkunft, Besonderheiten und Anwendungsbereichen. 
Abschließend werden Methoden zum Vergleich von Sprachmodellen und die im Projekt verwendeten Bewertungskriterien vorgestellt.

Allgemeine Funktionsweise von Large Language Models
---------------------------------------------------

Es sind KI-Systeme, die mithilfe tiefer neuronaler Netze Sprache verstehen und generieren können. 
Sie werden mit gigantischen Textmengen trainiert, um statistische Sprachmuster zu erlernen ` [1] <https://www.intel.de/content/www/de/de/learn/large-language-models.html>`_.
Ein LLM basiert heutzutage meist auf der Transformer-Architektur ` [2] <https://www.ibm.com/de-de/think/topics/transformer-model>`_.
Im Training lernt das Modell dabei, das jeweils nächste Wort (Token) in einem Satz vorherzusagen.
Durch die enorme Anzahl an Parametern, welche häufig viele Milliarden beträgt, können LLMs äußerst komplexe Muster speichern und menschenähnlich klingende Texte generieren ` [3] <https://openai.com/research/gpt-4>`_.

Wichtig ist, dass LLMs generalisierte Sprachkenntnisse aus ihren Trainingsdaten ziehen. 
Sie speichern nicht einfach alle Beispiele, sondern lernen abstrakte Zusammenhänge, z. B. können moderne LLMs dadurch vielfältige Aufgaben ohne spezialisierte Programmierung bewältigen, Fragen beantworten, bis hin zum Schreiben von Code oder kreativen Texten.

Vorstellung der im Projekt verwendeten Modelle
----------------------------------------------

Im Rahmen dieses Projekts wurden fünf verschiedene Sprachmodelle bzw. KI-Assistenten verglichen. Im Folgenden werden diese Modelle vorgestellt, inklusive ihrer Herkunft, besonderen Merkmale und typischen Anwendungsgebiete.

Gemini
~~~~~~

Gemini ist eine Familie multimodaler großer Sprachmodelle, die von Google DeepMind entwickelt wurde ` [4] <https://blog.google/technology/ai/google-gemini-ai/>`_.
Sie wurde erstmals Ende 2023 vorgestellt und gilt als Nachfolger von Googles früheren Modellen LaMDA und PaLM ` [5] <https://deepmind.google/technologies/gemini/>`_ und wurde als direkter Konkurrent zu OpenAIs GPT-4 positioniert ` [6] <https://www.theverge.com/2023/12/6/23990466/google-gemini-llm-ai-model>`_. 
Ein besonderes Merkmal von Gemini ist seine Multimodalität, da es nicht nur Text verstehen und erzeugen kann, sondern auch Bilder, Audio und andere Datenmodalitäten verarbeiten. 

Google hat Gemini in verschiedenen Größenordnungen veröffentlicht z. B. Gemini Ultra, Gemini Pro, Gemini Flash oder Gemini Nano, um unterschiedliche Einsatzzwecke abzudecken ` [7] <https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference?hl=de>`_.
Typische Anwendungsbereiche für Gemini sind die Integration in Suchmaschinen oder Assistenzsysteme, die komplexe Planungs- und Analyseaufgaben erledigen müssen, sowie Entwicklerwerkzeuge, die von den Kodierfähigkeiten des Modells profitieren.

Code Llama
~~~~~~~~~~

Code Llama ist ein von Meta AI im Jahr 2023 veröffentlichtes großes Sprachmodell, das speziell für Aufgaben im Bereich Programmierung und Quelltextgenerierung entwickelt wurde. 
Es handelt sich um eine Variante des Llama-2-Modells, die durch zusätzliches Training auf umfangreichen Code-Datensätzen verfeinert wurde ` [8] <https://ai.meta.com/blog/code-llama-large-language-model-coding/>`_.
Im Gegensatz zu allgemeinen LLMs ist Code Llama darauf optimiert, Programmcode in verschiedenen Sprachen wie z. B. Python, C++, Java, JavaScript, C# usw. zu erzeugen und zu verstehen ` [9] <https://huggingface.co/codellama>`_.
So kann das Modell nicht nur Code-Vervollständigung anbieten, sondern auch in natürlicher Sprache gestellte Fragen zu Code beantworten oder beim Debugging unterstützen. 

Meta hat Code Llama in mehreren Größen bereitgestellt, typischerweise mit 7, 13, 34 und bis hin zu 70 Milliarden Parametern.  
Für dieses Projekt wurde aus Ressourcengründen die 13B-Variante verwendet, da sie einen guten Kompromiss zwischen Leistungsfähigkeit und Laufzeit bietet.  
Besonders hervorzuheben ist, dass das Modell lokal auf eigener Hardware ausgeführt wurde im Rahmen der Versuchsdurchführung.
Typische Anwendungsbereiche von Code Llama sind Entwicklungsumgebungen und Chatbots für Programmierer, die automatisch Code-Vorschläge liefern, Funktionen implementieren oder bestehende Codeblöcke erklären sollen. 

DeepSeek
~~~~~~~~

DeepSeek ist ein neues großes Sprachmodell eines chinesischen Start-ups, das Ende 2024 auf sich aufmerksam machte. 
Die erste Version DeepSeek-R1 umfasst etwa 670 Milliarden Parameter, was es zum bis dahin größten frei verfügbaren Open-Source Sprachmodell machte ` [10] <https://www.pgrmt.com/en/blog/deepseek-r1-vs-chatgpt-o3-mini>`_.
Der große Vorteil ist, dass pro Anfrage immer nur die jeweils relevanten Teile des Modells aktiviert, sodass nicht alle 670 Mrd. Parameter gleichzeitig genutzt werden müssen ` [11] <https://www.scientificamerican.com/article/why-deepseeks-ai-model-just-became-the-top-rated-app-in-the-u-s/>`_. 
Dies ermöglicht eine sehr effiziente Inferenz, bei der trotzdem eine hohe Modellkapazität für komplexe Aufgaben bereitsteht. 

DeepSeek wurde mit vergleichsweise geringem Budget trainiert und dennoch erreichte es in ersten Benchmarks ähnliche Leistungen wie OpenAIs Modelle bei mathematischen Problemlösungen und Programmieraufgaben ` [12] <https://www.scientificamerican.com/article/why-deepseeks-ai-model-just-became-the-top-rated-app-in-the-u-s/>`_. 
Das Modell ist gratis verfügbar und kann von Nutzern heruntergeladen und lokal ausgeführt werden.
Zu den besonderen Stärken von DeepSeek zählen logisches Denken, Mathematik und Codierung, was es insbesondere für technische Anwendungen attraktiv macht. 
Typische Einsatzgebiete sind z. B. die Nutzung in Forschung und Lehre, als Grundlage für unternehmensspezifische Assistenten oder als Bestandteil komplexer Software-Lösungen.

ChatGPT-4o (OpenAI)
~~~~~~~~~~~~~~~~~~~

ChatGPT-4o, das „o“ steht für omni, ist die fortgeschrittene Generation des ChatGPT-Modells von OpenAI, die im Mai 2024 eingeführt wurde ` [13] <https://openai.com/index/hello-gpt-4o/>`_. 
GPT-4o stellt einen bedeutenden Entwicklungsschritt gegenüber GPT-4 dar und wurde als multilinguales und multimodales System konzipiert ` [14] <https://openai.com/index/hello-gpt-4o/>`_. 
Das bedeutet, ChatGPT-4o kann neben Text auch Bilder und Audio verstehen und generieren ` [15] <https://openai.com/index/hello-gpt-4o/>`_. So beherrscht es z. B. Bildanalyse und kann per Sprachsynthese antworten, was neue Interaktionsmöglichkeiten bietet. 

Außerdem verfügt das Modell über ein sehr großes Kontextfenster von bis zu 128.000 Token ` [16] <https://openai.com/index/hello-gpt-4o/>`_, dadurch kann ChatGPT-4o deutlich mehr Input auf einmal berücksichtigen.
Die Architektur und das Training von GPT-4o wurden außerdem auf Effizienz optimiert, d. h. die Abfrageantworten werden schneller geliefert und die Nutzung über die API ist kostengünstiger als bei früheren GPT-4-Versionen ` [17] <https://openai.com/index/hello-gpt-4o/>`_. 

Anwendungsbereiche sind praktisch alle Gebiete, in denen hochentwickelte Sprach-KI benötigt wird: 

- Anspruchsvolle Dialogsysteme
- Content-Generierung
- Übersetzung
- Analyse von Text- und Bilddaten
- Programmierhilfe
- ...

Durch seine hohe Kapazität liefert ChatGPT-4o in der Regel sehr ausführliche und kontextsensitive Antworten und kann komplexe Anfragen besser bewältigen als kleinere Modelle.

ChatGPT-mini-high (OpenAI)
~~~~~~~~~~~~~~~~~~~~~~~~~~

ChatGPT-mini-high bezeichnet eine kleinere, kostenoptimierte Variante von OpenAIs ChatGPT-Modell, die dennoch über erweiterte Fähigkeiten verfügt. 
OpenAI veröffentlichte im Jahr 2024 mit GPT-4o mini ein Modell, das nur etwa 8 Milliarden Parameter umfasst und wesentlich schneller sowie günstiger zu betreiben ist als GPT-4o ` [18] <https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/>`_. 
Dieses „Mini“-Modell ersetzte das vorherige GPT-3.5-Turbo als Standard für den ChatGPT-Dienst und erwies sich dabei als leistungsstark ` [19] <https://platform.openai.com/docs/models/gpt-4o-mini>`_. 
Die Bezeichnung mini-high deutet darauf hin, dass diese kleine Modellvariante in einem High-Performance-Modus läuft. 

In der Praxis bedeutet das, dass ChatGPT-mini-high für komplexe Eingaben mehr Rechenzeit und ausgefeiltere Strategien aufwendet, um möglichst hochwertige Antworten zu generieren. 
OpenAI führte ChatGPT-mini-high Anfang 2025 als frei zugängliche ChatGPT-Variante mit verbesserten logischen Fähigkeiten ein, als Antwort auf die neue Konkurrenz wie z. B. DeepSeek ` [20] <https://www.theverge.com/news/603849/openai-o3-mini-launch-chatgpt-api-available-now>`_. 
Typische Anwendungsfälle für ChatGPT-mini-high sind allgemeine Chatbot-Anfragen im Alltagsgebrauch, bei denen eine hohe Antwortqualität gefragt ist, aber zugleich die Kosten und die Antwortzeit niedrig gehalten werden sollen. 
Es eignet sich z. B. für Endnutzer-Anwendungen und Assistenten, die auf vielen Geräten laufen, da es weniger Ressourcen benötigt, aber dennoch fortschrittliches Verständnis und gute Antworten liefert.

Methoden zum Vergleich von Sprachmodellen
-----------------------------------------

Um verschiedene KI-Assistenten objektiv zu vergleichen, benötigt man definierte Bewertungskriterien und Testmethoden. 
In diesem Projekt wurden die Antworten der Modelle anhand mehrerer Qualitätsaspekte beurteilt:

Antwortqualität
~~~~~~~~~~~~~~~

Wie gut beantwortet das Modell die gestellte Frage oder erfüllt die Anforderung?    
Dabei spielen Faktoren wie Relevanz, Vollständigkeit und Verständlichkeit der Antwort eine Rolle. 
Eine hohe Antwortqualität bedeutet, dass die Ausgabe für den Nutzer nützlich und zufriedenstellend ist. Vor allem beim Coden wird hoher Wert auf Funktionalität gelegt. 

Kreativität
~~~~~~~~~~~

Inwieweit bringt das Modell originelle oder einfallsreiche Formulierungen und Ideen hervor?  
Ein kreativer KI-Assistent liefert nicht nur Standardantworten, sondern überrascht mit neuartigen Ansätzen, Bildern oder Beispielen. 
Werden auf traditionelle Algorithmen zur Problemlösung zurückgegriffen oder Alternativmethoden individuell auf die vorliegende Aufgabe geschaffen?

Genauigkeit
~~~~~~~~~~~

Die faktische Richtigkeit und Präzision der Inhalte. 
Ein Modell mit hoher Genauigkeit und Funktionalität gibt korrekte Informationen wieder und vermeidet Fehler oder widersprüchliche Aussagen. 
Insbesondere bei Codebeispielen und Berechnungen ist dieser Faktor entscheidend. 
Da LLMs anfällig für sogenannte Halluzinationen sind, wurde im Projekt genau darauf geachtet, ob die Modelle verlässliche Angaben machen.

Zur Vergleichsmethode
~~~~~~~~~~~~~~~~~~~~~

Alle Modelle erhielten im Test die gleichen Eingaben, sodass ihre Ausgaben direkt gegenübergestellt werden konnten und auch immer direkt der erste Prompt unverändert benutzt. Die Bewertung erfolgte nach den obigen Kriterien, teils durch unser menschliches Empfinden, teils unterstützt durch automatisierte Metriken wie selbst erstellte Tests zur groben Einordnung. 

Ein strukturierter Vergleich anhand dieser Qualitätsmerkmale ermöglicht es, die Stärken und Schwächen der einzelnen KI-Assistenten herauszuarbeiten. 
Auf diese Weise gewinnt man ein umfassendes Bild davon, welches Modell sich für welche Arten von Aufgaben am besten eignet und wo eventuell Verbesserungsbedarf besteht.
