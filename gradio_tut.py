import os
import socket
import subprocess
import gradio as gr



def kill_port(port):
    """Kills the process running on the given port."""
    try:
        # Use lsof to find the process using the port
        result = subprocess.check_output(f"lsof -t -i:{port}", shell=True)
        pids = result.decode().strip().split('\n')
        for pid in pids:
            print(f"Killing process on port {port}: PID {pid}")
            os.kill(int(pid), 9)
    except subprocess.CalledProcessError:
        # lsof returns non-zero exit code if nothing is using the port
        print(f"No process running on port {port}")
        
        
def greet(name):
    return f"Hello {name}!"

with gr.Blocks() as demo:
    chatbot = gr.Chatbot(
    title="Chatbot",
    description="A simple chatbot example",
    theme="default",
    )
    
    chat_state = gr.State([])
    
    
    
    







kill_port(7860)  # Ensure port 7860 is free before launching

demo.launch(server_port=7860, server_name="127.0.0.1", share=False, inbrowser=False)