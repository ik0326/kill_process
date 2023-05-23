import streamlit as st
import pyperclip

def text_to_list(text):
    lines = text.split('\n')
    return lines

def split_text(text):
    a = [i.split()[0] for i in text if i] 
    return a

def main():
    st.title("Kill Process Command App")
    st.subheader("Paste the output from typing 'ps' in your terminal window into the text box below. You will get a command to terminate the entire process.") 
    #input text feild
    process_name = st.text_area("Enter the process name to kill",value=""" 1353 ttys001    0:00.22 /Applications/Xcode.app/Contents/Developer/usr/bin/xcd
69634 ttys020    0:00.03 /bin/zsh -il
69737 ttys020    0:03.84 /opt/homebrew/Cellar/python@3.10/3.10.8/Frameworks/Pyt
69742 ttys020    0:00.00 <defunct>""")

    #print input text

    if process_name:
        p = text_to_list(process_name)
        process_name = split_text(p)

        output_text = "kill -9 " + " ".join(process_name)
        st.write(output_text)

        #if button is clicked, copy the input text to clipboard

        if st.button("copy"):
            pyperclip.copy(output_text)
            st.success("Copied to clipboard")
        elif not process_name:
            st.error("Please enter the process name")
        
    

if __name__ == "__main__":
    main()