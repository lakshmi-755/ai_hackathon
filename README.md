# ai_hackathon
problem statement selected is 
"AI POWERED STORY GENERATOR FOR KIDS USING IMAGES AS INPUT"
my problem solution approach :
obtaining text description from image and obtaining key words from the text description through nlp preprocessing techniques and td-idf vectoriser
and then passing this keywords to a open api model that is finetuned on shortstories dataset on kaggle  to generate a short story 

1) I wanted to use deeplearning and nlp techniques  like encoder decoder,lstm i want to fine tune them with the suitable parameters such that the releveant story can be genereated.but due to  time and computational constraints .iam using a pretrained model called "BlipProcessor".i  have imported that model  and succesfully generated description of the inputed image
 Using the BLIP model from Hugging Face provides a powerful,pre-trained solution for generating captions for images.It abstracts away the complexity of training an image captioning
model,allowing you to focus on using the model for practical applications.This approach works well without needing a custom dataset, andit gives you high-quality captions based on the visual content of
the image  thats why this is used

2) then from the obtained text description i want to apply nlp preprocessing techniques like stop words removal ,stemming ,lemmatisation and to obtain key words TF-IDF Vectorizer and after obtainning key words the
3) iam fine tuning the open api model on the shortstories dataset on kaggle  to generate a short story
4) 
   
