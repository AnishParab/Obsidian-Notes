# **Topics Covered**
[[#LLM's]]
[[#Setup, Integration, Workflow and Deployment]]
- [[#> **OpenAI**]]
- [[#> **Google AI Studio**]]
- [[#> **Ollama**]]
- [[#> **Hugging Face**]]
- [[#> **Claude-Code and Vibe-Coding Tools**]]
[[#LLM - Context]]
- [[#> **Prompt Context**]]
- [[#> **Web-Search Context using `Tavily`**]]

---
# LLM's
[[Index_LLM]]
##### Basics
[[Applied_AI_LLM_What_is_LLM]]
[[Applied_AI_LLM_GPT_Architecture]]
[[Applied_AI_LLM_Transformer_Google_vs_GPT]]
##### Tokens
[[Applied_AI_LLM_Tokens]]
[[Applied_AI_LLM_Tokens_Tiktokenizer_Website]]
[[Applied_AI_LLM_Tokens_Tokenizer_Implementation]]
[[Applied_AI_LLM_Tokens_Tokenizer_Hugging_Face_Implementation]]
##### Google - Attention is all you need
[[Applied_AI_LLM_Attention_Is _All_You_Need_Google]]
[[Applied_AI_LLM_Vector_Embeddings_Tensorflow_Dataset]]
[[Applied_AI_LLM_Positional_Encoding]]
[[Applied_AI_LLM_Self_Attention]]
[[Applied_AI_LLM_Multi-Head_Attention]]

---
# Setup, Integration, Workflow and Deployment
## > **OpenAI**
[[Index_OpenAI]]
##### OpenAI Setup and Config
[[Applied_AI_OpenAI_Account_Setup_and_Config]]

---
## > **Google AI Studio**
[[Index_Google_Gemini_AI_Studio]]
##### Gemini API Key
[[Applied_AI_Google_Gemini_AI_Studio_API_KEY]]
##### Gemini Setup and Config
[[Applied_AI_Google_Gemini_Account_Setup_and_Config]]
##### Gemini model running on OpenAI API - Setup and Config
[[Applied_AI_Google_Gemini_Compatible_OpenAI_API_Setup]]

---
## > **Ollama**
[[Index_Ollama]]
##### Ollama Documentation
[[Applied_AI_Ollama_Official_Website]]
##### Ollama
[[Applied_AI_Ollama_What_is_Ollama]]
##### Ollama Models
[[Applied_AI_Ollama_Pull_and_Run_Models]]
##### Local LLM Deployment and API Integration
[[Applied_AI_Why_Docker_Environment_for_Ollama]]
[[Applied_AI_Ollama_Models_with_Docker_Runner]]
[[Applied_AI_Configuring_OpenWebUI_with_Ollama_Backend]]
[[Applied_AI_Ollama_and_FastAPI_Setup]]

---
## > **Hugging Face**
[[Index_Hugging_Face]]
##### Hugging Face Website
[[Applied_AI_Hugging_Face_Website]]
##### Hugging Face API Keys
[[Applied_AI_Hugging_Face_API_Keys]]
##### Hugging Face
[[Applied_AI_What_is_Hugging_Face]]
##### Hugging Face Models
[[Applied_AI_Hugging_Face_Models]]
[[Applied_AI_Hugging_Face_Models_How_to_Use]]
##### Hugging Face - Transformers
[[Applied_AI_Hugging_Face_Models_Tokenizer_Model]]

---
## > **Claude-Code and Vibe-Coding Tools**
[[Index_Claude_Code]]
##### Claude-CLI and Ollama Setup and Config
[[Applied_AI_Claude_Code_CLI_Setup_and_Installation]]
[[Applied_AI_Claude_Code_and_Ollama_Models_Setup_and_Installation]]

> **Section 0**: *INTRODUCTION and FEATURES*
##### Claude Code Introduction
[[Applied_AI_Claude_Code_Introduction]]
[[Applied_AI_Claude_Code_Why_use_it]]
[[Applied_AI_Claude_Code_Why_use_it_with_Ollama]]
##### Claude Code Working
[[Applied_AI_Claude_Code_Working_Agentic_Loop]]
[[Applied_AI_Claude_Code_Working_Two_Components_of_Claude]]
##### Built-in Slash Commands
[[Applied_AI_Claude_Code_Built-in_Slash_Commands]]
##### Claude Code Ergonomics
[[Applied_AI_Claude_Code_Ergonomics_login]]
[[Applied_AI_Claude_Code_Ergonomics_logout]]
[[Applied_AI_Claude_Code_Ergonomics_exit_flag]]
[[Applied_AI_Claude_Code_Ergonomics_bash_mode]]
[[Applied_AI_Claude_Code_Ergonomics_voice_mode]]
[[Applied_AI_Claude_Code_Ergonomics_set_theme]]
[[Applied_AI_Claude_Code_Ergonomics_upload_images]]
##### Claude Code Accessibility
[[Applied_AI_Claude_Code_Accessibility]]

> **Section 1**: *MODELS*
##### Claude Models
[[Applied_AI_Claude_Code_Models_flagship_models]]
[[Applied_AI_Claude_Code_Models_switch_models]]
##### Model Usage Status
[[Applied_AI_Claude_Code_Model_Usage_status]]
[[Applied_AI_Claude_Code_Model_Usage_extra_top_up]]
[[Applied_AI_Claude_Code_Model_Usage_statistics]]
[[Applied_AI_Claude_Code_Model_Usage_detailed_report_insights]]
##### **Workflow for Model Usage**
[[Applied_AI_Claude_Code_Model_Usage_Workflow]]

> **Section 2**: *TOOLS*
##### Claude Built-in Tools
[[Applied_AI_Claude_Code_Tools]]
[[Applied_AI_Claude_Code_Tools_Built_in]]
##### Custom Tools
[[Agentic_AI_Claude_Code_Tools_Custom_Tools]]

> **Section 3**: *SESSIONS*
##### Claude Sessions
[[Applied_AI_Claude_Code_Sessions_and_Session_Saved_Location]]
[[Applied_AI_Claude_Code_Sessions_saved_location]]
[[Applied_AI_Claude_Code_Sessions_resume]]
[[Applied_AI_Claude_Code_Sessions_switch]]
[[Applied_AI_Claude_Code_Sessions_rename]]
[[Applied_AI_Claude_Code_Sessions_btw_questions]]
[[Applied_AI_Claude_Code_Sessions_export]]
[[Applied_AI_Claude_Code_Sessions_clear]]
##### **Workflow for Sessions**
[[Applied_AI_Claude_Code_Sessions_Workflow]]

> **Section 3**: *FOLDER STRUCTURE*
##### `.claude/`, `~/.claude/`
[[Applied_AI_Claude_Code_CLAUDE_Folder_Introduction]]
[[Applied_AI_Claude_Code_CLAUDE_Folder_Types]]
##### `.claude/` - **CONTEXT and TOKEN Usage: 1**
[[Applied_AI_Claude_Code_CLAUDE_Folder_Content_and_Good_Practices]]
##### `~/.claude/projects/` - Session Store
[[Applied_AI_Claude_Code_HOME_CLAUDE_PROJECTS_session_storage]]
##### Permissions - `settings.json`
##### Permissions - `settings.local.json`
[[Applied_AI_Claude_Code_Change_Settings_config_flag]]
[[Applied_AI_Claude_Code_Set_Permissions]]
[[Applied_AI_Claude_Code_Set_Permissions_File_settings_local_json]]
###### Custom Slash Commands
[[Applied_AI_Claude_Code_Custom_Slash_Commands]]
##### Rules
##### Skills
##### Sub-agents
[[Applied_AI_Claude_Code_Sub_Agents]]
##### Prompting **(IMPORTANT)**
[[Applied_AI_Claude_Code_Prompting_prompt_file]]
[[Applied_AI_Claude_Code_Prompting_deterministic_file_navigation]]

> **Section 2**: *MEMORY*
##### `CLAUDE.md`, `CLAUDE.local.md`,  `.claudeignore` - **CONTEXT and TOKEN Usage: Step 2**
[[Applied_AI_Claude_Code_CLAUDE_md_File_Introduction]]
[[Applied_AI_Claude_Code_CLAUDE_md_File_Creation]]
[[Applied_AI_Claude_Code_CLAUDE_md_File_init_working]]
[[Applied_AI_Claude_Code_CLAUDE_md_File_Content_and_Structure]]
[[Applied_AI_Claude_Code_CLAUDE_md_File_Types]]
[[Applied_AI_Claude_Code_CLAUDE_LOCAL_md_File]]
[[Applied_AI_Claude_Code_CLAUDE_md_Global_File]]
[[Applied_AI_Claude_Code_CLAUDE_md_Subdirectory_File]]
[[Applied_AI_Claude_Code_CLAUDE_md_File_less_rule_count]]
[[Applied_AI_Claude_Code_CLAUDE_md_File_important_tag]]
[[Applied_AI_Claude_Code_CLAUDEIGNORE_File]]

[[Applied_AI_Claude_Code_CLAUDE_md_File_Good_Practices]]
##### Auto-memory
[[Applied_AI_Claude_Code_Auto_Memory_Introduction]]
[[Applied_AI_Claude_Code_Auto_Memory_file_location]]
[[Applied_AI_Claude_Code_Auto_Memory_update_memory]]


> **Section 6**: *Context Window Management*
##### Context Window Management
[[Applied_AI_Claude_Code_Context_Window_Management_Introduction]]
[[Applied_AI_Claude_Code_Context_Window_Management_types_of_contexts]]
[[Applied_AI_Claude_Code_Context_Window_Management_why_it_matters]]
[[Applied_AI_Claude_Code_Context_Window_Management_token_usage_reality]]
[[Applied_AI_Claude_Code_Centext_Window_Management_compaction]]
##### Context Window Management: Good Practices - **CONTEXT and TOKEN Usage: Step 5**
[[Applied_AI_Claude_Code_Context_Window_Management_Good_Practices]]

> **Section 7**: *Claude Code SDK*

###### Claude Agent SDK

---
# LLM - Context
[[Index_LLM_Context]]
## > **Prompt Context**
[[Index_Prompt_Engineering]]
##### Prompt Engineering Heirarchy
[[Applied_AI_Prompt_Engineering_Prompt_Heirarchy]]
##### Assistant Prompts: Maintaining Contexts
[[Applied_AI_Prompt_Engineering_Assistant_Prompts]]
[[Applied_AI_Prompt_Engineering_Assistant_Prompts_Code]]
###### User Prompts: Intent and Tasks
[[Applied_AI_Prompt_Engineering_User_Prompts]]
[[Applied_AI_Prompt_Engineering_User_Prompts_CLI_Chat_Interface]]
###### Developer Prompts: Pydantic and Applied AI
[[Applied_AI_Prompt_Engineering_Developer_Prompts]]
[[Applied_AI_Prompt_Engineering_Developer_Prompt_Role_Based_Access]]
[[Applied_AI_Prompt_Engineering_Developer_Prompt_RBAC_using_Pydantic]]
###### System Prompts and Types: Model Behavior Governer
[[Applied_AI_Prompt_Engineering_System_Prompts]]
[[Applied_AI_Prompt_Engineering_Zero_Shot_Sytem_Prompts]]
[[Applied_AI_Prompt_Engineering_One_Shot_System_Prompts]]
[[Applied_AI_Prompt_Engineering_Few_Shot_System_Prompts]]
[[Applied_AI_Prompt_Engineering_Few_Shot_System_Prompts_Structured_Outputs]]
[[Applied_AI_Prompt_Engineering_Explicit_Chain_of_Thought_COT_Prompts]]
[[Applied_AI_Prompt_Engineering_COT_Prompts_Thinking_Mechanism]]
[[Applied_AI_Prompt_Engineering_Persona_Based_Prompts]]
##### Prompt Serialization and Instruction Formats
[[Applied_AI_Prompt_Engineering_Prompt_Serialization_Style_Alpaca]]
[[Applied_AI_Prompt_Engineering_Prompt_Serialization_Style_ChatML]]
[[Applied_AI_Prompt_Engineering_Prompt_Styles_ChatML_vs_Alpaca]]
[[Applied_AI_Prompt_Engineering_Prompt_Serialization_Style_INST]]
[[Applied_AI_Prompt_Engineering_Prompt_Styles_INST_vs_ChatML_vs_Alpaca]]

---
## > **Web-Search Context using `Tavily`**
[[Index_Tavily]]
[[Applied_AI_Tavily_Official_Documentation]]
##### Travily Introduction
[[Tavily_Introduction]]
[[Tavily_Use_Cases]]
[[Tavily_Search_API_Working]]
##### Tavily Installation and API Setup
[[Tavily_pip_Installation]]
[[Tavily_API_Key]]
##### Tavily Authentication
[[Tavily_Authentication]]
##### Tavily Project Tracking
[[Tavily_Project_Tracking]]
##### Travily Use-cases
[[Tavily_Search_the_Web]]
[[Tavily_Extract_Web_Pages]]
[[Tavily_Crawl_Web_Pages]]
[[Tavily_Map_Web_Pages]]
[[Tavily_Create_Research_Talk]]
##### Tavily Rate Limits
[[Tavily_Rate_Limits]]
##### Tavily Mini-Project
[[Tavily_News_Digest_App]]

---
# Agentic AI
[[Applied_AI_Agentic_AI_Types_of_Agents]]
[[Applied_AI_Agentic_AI_Code_Implementation]]
###### Pydantic and OpenAI API
[[Applied_AI_Structured_Outputs_with_Pydantic]]
###### Example
[[Applied_AI_Building_Claude_Code_Basic_Code]]

---
# RAG and LangChain
### RAG
[[Applied_AI_RAG_Systems_Core_Problems]]
[[Applied_AI_Naive_Retrieval_Based_Approach_Context_Window_Problem]]
###### RAG Pipelines
[[Applied_AI_RAG_Phases]]
[[Applied_AI_RAG_Pipeline_Indexing_Workflow]]
[[Applied_AI_RAG_Retreival_Mechanism]]
### Vector DataBases
###### Vector Databse Setup
[[Applied_AI_Local_Vector_DB_Quadrant_Setup_with_Docker_Compose]]
### LangChain
###### LangChain
[[Applied_AI_LangChain_Introduction]]
[[Applied_AI_LanChain_Installation_and_Setup]]
[[Applied_AI_LanChain_PDF_Mini_Project]]
[[Applied_AI_LangChain_PDF_Project_But_Production_Level_Code]]
### Scalable RAG
###### Sync v/s Async in RAG
[[Applied_AI_RAG_Architectures_Sync_vs_Async]]
[[Applied_AI_RAG_Queues_in_System_Design_for_Async_Architecture]]
[[Applied_AI_Asynchronous_RAG_Overall_File_System]]
###### RQ in Python, Redis, Valkey
[[Applied_AI_Python_Redis_Valkey_Qdrant_Docker_Setup]]
[[Applied_AI_Python_RQ_Distribute_Queues_Client_RQClient_Setup]]
###### Worker Orchestration
[[Applied_AI_RAG_Queues_Worker_Orchestration]]
###### FastAPI and RAG
[[Applied_AI_RAG_FastAPI_Setup]]
[[Applied_AI_Asynchronous_Message_Enqueing_with_FastAPI_Server]]
[[Applied_AI_FastAPI_Polling_Dequeuing_Messages_from_Async_Queues]]
[[Applied_Ai_Running_and_Scaling_Worker_Nodes_for_Background]]

---
# Multi Modal Agent
[[Applied_AI_Multi_Modal_Agents]]

---
# Fine-Tuning LLM Models
##### Quantization
[[Applied_AI_Fine_Tuning_Quantization]]


---
