tools = [
       Tool(
           name="Python Agent",
           func= code_creator,
           description="""useful when you need to transform natural language to python and execute the python code,
                         returning the results of the code execution
                         DOES NOT ACCEPT CODE AS INPUT""",
       ),
       Tool(
           name="CSV Agent",
           func= csv_reader,
           description="""useful when you need to answer question over episode_info.csv file,
                        takes an input the entire question and returns the answer after running pandas calculations""",
       ),
   ]


base_prompt = hub.pull("langchain-ai/react-agent-template")
prompt_val = base_prompt.partial(instructions="")


router_agent = create_react_agent(
   prompt = prompt_val,
   llm = ChatOpenAI(temperature=0, model='gpt-4-turbo'),
   tools = tools
)

router_executor = AgentExecutor(agent=router_agent, tools=tools, verbose=True)


actual_value = router_executor.invoke(
           {
               "input": "which season has the most episodes?",
               
           }

       )
