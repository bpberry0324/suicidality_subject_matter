# On Suicidality Subject Matter Detection

The purpose of this study is to create a predictive model that assesses text and detects in its subject matter content that relates to suicidality, and to examine the ways in which the results can facilitate analysis and prevention.

### Table of Contents:

- Part I: Summary of Findings
- Part II: File Directory
- Part III: Main Datasets Used
- Part IV: Conclusion

## Part I: Summary of Findings

While sufferers of depression are not and must not be assumed inherently suicidal, depression can often serve as a contributing cause in suicidality. Thus, questions arise: Can reliable means be developed to detect distinctions between subject matter authored by sufferers of depression or that remains within the threshold of depression and subject matter that crosses a threshold into suicidality, or at least whose focus is suicidality? What would such means looks like, and to what uses might we use them? Most importantly, how might the development and improvement of such detection aid in future suicide prevention?

This study aims primarily to lay a foundation for answering these questions by developing a functional predictive model that can distinguish reliably between text bodies on either side of this threshold (i.e. depression and suicidality) and to allow the findings and corrollary Streamlit application to act as a stepping stone for further inquiry.

It must be stated that nothing within this study ought to be taken as the equivalent of or a substitute for real licensed medical treatment.

During the course of the project, the data (consisting of text posts collected by Nikhileswar Komati from r/SuicideWatch and r/depression using the PushShift API) was fit to many binary classification models, in a variety of forms, or having undergone a variety of different "versions" of preprocessing. Ultimately, the strongest model was a logistic regression model that used lemmatized, words-only versions of the text with stopwords removed, vectorized according to term frequency. The Streamlit app features an input text field wherein a user may input a block of text, as well as an additional field where a probability threshold can be added. The text in question is then run through the pickled logistic regression model and then classified either as containing subject matter related to suicidality or not , depending on this threshold. The threshold option exists to allow users the ability to optimize accuracy and recall calibration according to their specific use cases.

Coefficients of the final model align closely with what the available medical literature suggests about suicidality. (More on this in the presentation PDF and the main Jupyter notebook.)

## Part II: File Directory

|File or Folder|Description|
|---|---|
|app.py|the code file for the Streamlit app that corresponds to this study|
|appendices/app|subdirectory that includes the notebook in which the final model is pickled for the app|
|appendices/modeling|subdirectory that includes upwards of twenty notebooks used for selecting and fine-tuning the best predictive model|
|appendices/preprocessing|subdirectory that records the cleaning and initial exploratory analysis, as well as the engineering of the eight forms in which the text was fit to the initial models|
|datasets|directory that includes the data files used for feature engineering and in the creation of the predictive model|
|images|directory that includes images used by the Streamlit app|
|main.ipynb|the project's primary Jupyter notebook, providing concise explanations of its approach and findings (with code)|
|presentation.pdf|a PDF version of the slide presentation given in conjunction with the completion of this project|
|README.md|a summary of the project's aims, findings, data dictionary, and conclusions|

## Part III: Main Datasets Used

- [`down_sample.csv`]('datasets/down_sample.csv'): a more manageable fraction of `full.csv` (30,000 combined text entries) in eight different preprocessed versions
- [`full.csv`]('datasets/full.csv'): the most complete (relevant) dataset of this project, including all of over 700,000 combined text entries in eight different preprocessed versions
- [`source_data.csv`]('datasets/source_data.csv'): the initial dataset scraped by Nikhileswar Komati, and the foundational dataset for this project

Below is a list of relevant features included in `full.csv` and `down_sample.csv` as they relate to the final predictive model:

|Feature|Type|Dataset|Description|
|---|---|---|---|
|comp_lem|string|down_sample.csv|the title and post body of each entry, lemmatized words and potentially significant digits|
|comp_stem|string|down_sample.csv|the title and post body of each entry, stemmed words and potentially significant digits|
|simp_lem|string|down_sample.csv|the title and post body of each entry, words only (lemmatized)|
|simp_stem|string|down_sample.csv|the title and post body of each entry, words only (stemmed)|
|Subreddit|int|down_sample.csv|the binarized target class for the final model, with `0` for `r/depression` and `1` for `r/SuicideWatch`|
|unst_comp_lem|string|down_sample.csv|down_sample.csv|the title and post body of each entry, lemmatized words (with English stopwords removed) and potentially significant digits|
|unst_comp_stem|string|down_sample.csv|the title and post body of each entry, stemmed words (with English stopwords removed) and potentially significant digits|
|unst_simp_lem|string|down_sample.csv|the title and post body of each entry, words only (lemmatized) with English stopwords removed|
|unst_simp_stem|string|down_sample.csv|the title and post body of each entry, words only (stemmed) with English stopwords removed|

## Part IV: Conclusion

Finally, the model works. Its implications are again somewhat unclear and would require further inquiry to iron out. Suicidality as subject matter can be said to be reliably detectable, but to what degree does suicidality as subject matter correlate with suicidality as such? This is a fair question, but a cursory perusal of the data suggest that the correlation in many cases is indeed present. More data from additional sources could fit to a model to make it more well-rounded, helping to bolster its predictive power in relation to a somewhat nebulous concept.

Could further developments connect specific terms with higher coefficients to known warning signs of suicidality, so that users might receive an output of what to read for in their input? This might be possible, but it also enters the realm of "diagnosis", and therefore must be treated with the greatest caution. Could known cases of suicide provide data that might be fit to time series models? Again, sensitivty to unforeseen externalities is paramount.

As it stands, the model and the Streamlit app form a foundation on which to build in exploring further.
