from flask  import Flask, render_template,request

app=Flask(__name__)

@app.route("/")
def index():
    #index.html has 3 text boxes (Input para, min_len, max_len) and a Summarize command button
    return render_template("index.html")

@app.route("/summarize/<int:max_len>_<int:min_len>",methods="POST")
def summarize(min_len,max_len):

        '''
        Call a function here to get different summarization of different sub-paragraphs:
            A paragraph with bulletin points gets one summary
            A para with subparagraphs gets multiple one-liner summaries

            incorporating this will change the else condition below
        '''
        if request.method=="GET":
            return render_template("error.html",message="Please provide an input")
        else:
            paragraph=request.form.get("paragraph")
            #
            para_summarized=summarizer(paragraph,max_length=max_len,min_length=min_len)
            return render_template("summarized.html",output=para_summarized,input=paragraph,max_length=max_len,min_length=min_len)
            #summarized.html has the same layout as index.html except the output summarized para


'''
- how to pass paragraphs into summarizer:
By using noSQL/request method/as an argument?
Explore This!

- how to ensure that the summarizer obj is up and running. New instance should not be created.

- check feasibiity of sagemaker.

- Start using Git.

- how to ensure system geenrates summary of an optimal max_length

- Call a function here to get different summarization of different sub-paragraphs:
    A paragraph with bulletin points gets one summary
    A para with subparagraphs gets multiple one-liner summaries

    incorporating this will change the else condition below
'''
if __name__=="__main__":
    app.run(port=82,debug=True)
