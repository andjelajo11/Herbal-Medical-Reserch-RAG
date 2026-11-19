# 🌿💊🌿💊 Herbal-Medical-Reserch-RAG 🌿💊🌿💊


A Retrieval-Augmented Generation (RAG) application designed to help users explore scientific research on supplements and medicinal herbs in relation to specific health conditions.

The project aims to make medical research more accessible by retrieving relevant scientific publications and presenting research-backed information with references to the original sources.

## Overview

Finding reliable scientific information about supplements and medicinal herbs can be challenging. Relevant evidence is often distributed across multiple research publications, making it difficult to identify and review sources related to a particular health condition.

This project explores how Large Language Models (LLMs), semantic search, keyword search and Retrieval-Augmented Generation (RAG) can support the discovery of relevant medical research.

Users can submit queries about a health condition, supplement, or herb. The system retrieves relevant research material and uses it as context for generating responses, with an emphasis on providing traceable scientific references.

## Key Features

- **Research Retrieval:** Retrieve scientific publications relevant to user queries about supplements, herbs, and health conditions.
- **Semantic Search:** Identify relevant research based on meaning and context rather than relying exclusively on exact keyword matches.
- **RAG Pipeline:** Combine retrieved research material with LLMs to generate context-aware responses.
- **Scientific References:** Present supporting research citations so users can investigate the original publications.
- **Health Research Exploration:** Explore the relationship between specific health conditions and supplements or medicinal herbs.

## Technology Stack

🌿 **Python** – Application logic and backend development.
🌿 **Retrieval-Augmented Generation (RAG)** – Grounding generated responses in retrieved research material.
🌿 **Weaviate** – Vector database for storing and retrieving research embeddings.
🌿 **Large Language Models (LLMs)** – Context-aware response generation.
🌿 **Semantic Search** – Retrieval of relevant research publications.

*The technology stack will be expanded as the project develops.*

## How It Works

The application follows a RAG-based workflow:

1. **User Query:** The user submits a question about a health condition, supplement, or medicinal herb.
2. **Research Retrieval:** The system searches the available research collection for relevant scientific publications.
3. **Context Preparation:** Retrieved research material is processed and provided as context to the language model.
4. **Response Generation:** The LLM generates a response based on the retrieved information.
5. **Citation Presentation:** Relevant scientific references are presented to help users consult the original research.

## Project Goals

🌿 Explore practical applications of RAG in health-related research.
🌿 Improve access to scientific literature through semantic information retrieval.
🌿 Encourage evidence-based exploration by connecting generated responses to scientific sources.
🌿 Investigate how AI can support the interpretation and discovery of interdisciplinary medical research.

## Responsible Use

This project is intended for research exploration and informational purposes only.

It is not a medical diagnostic tool and does not provide personalized medical advice or treatment recommendations. Retrieved publications and generated responses should be evaluated critically, and health-related decisions should be discussed with qualified healthcare professionals.

The presence of a scientific citation does not necessarily mean that a study supports a particular claim or establishes clinical effectiveness.

## Project Status

🚧 Work in progress.

Features, retrieval capabilities, and research-source coverage are being developed and refined.

---

**Author:** Anđela Jovanović  
