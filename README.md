# DC-ISP
Regarding the production of Chinese adversarial texts, please refer to: https://github.com/QData/TextAttack/blob/master/docs/2notebook/Example_6_Chinese_Attack.ipynb

You should install OpenPrompt https://github.com/thunlp/OpenPrompt

First, Predict initial pseudo-label for the target domain from source domain data.

Second, Adjust initial target domain data pseudo-label, divide target domain data and iterative training model.

Then, Adjust all target domain data pseudo-label and voted invariant label.

Final, Average the experimental results three times.

Note that the file paths should be changed according to the running environment.

example shell scripts:

python fewshot.py --result_file ./output_fewshot.txt --dataset newsgroups1 --template_id 0 --seed 144 --shot 20 --verbalizer manual
python 1-2.py
python 3rep_train.py
python 4ccover.py
python 5together.py
python 6final_train.py
