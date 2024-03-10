#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
#--Add the input path with file name 
option_csv = (r"D:\Cdac\Python\workspace\Option file\20_Options.csv")
old_option_file = (r"D:\Cdac\Python\workspace\Option file\20_Options1.xlsx")
productxfeature_csv = (r"D:\Cdac\Python\workspace\Option file\40_ProductsXFeatures.csv")

#--Add the output path with file name 
Output_option_path = r"D:\Cdac\Python\workspace\Option file\20_Options.xlsx"
Output_pxf_path = r"D:\Cdac\Python\workspace\Option file\40_ProductsXFeatures.xlsx"


# In[82]:


option_df = pd.read_csv(option_csv)
option1_df = pd.read_excel(old_option_file)
product_df = pd.read_csv(productxfeature_csv)


# In[83]:


option_df = option_df.drop(option_df[option_df["Code"].str.contains("AQTY")].index)


# In[84]:


option_df = option_df.fillna('not_required')


# In[85]:


option_df = option_df.drop(option_df[option_df['Parent'].str.contains('AQTY')].index)


# In[86]:


option_df['ShortDescription_en-US'] = ""
option_df['IsFeatureOptional'] = ""
option_df['IsDefault']=""
option_df = option_df.replace('not_required','')
option_df['Description_en-US'] = option_df['Description_en-US'].str.replace(r'\s*\[.*?\]$','',regex = True)


# In[87]:


option_df['merged'] = option_df['Code'].str.cat(option_df['Type'])


# In[88]:


option_df = option_df.drop(option_df[option_df['Code'].str.contains('-EO_17')].index)
option_df = option_df.drop(option_df[option_df['Code'].str.contains('-EO_18')].index)


# In[89]:


option1_df['merged'] = option1_df['Code'].str.cat(option1_df['Type'])
option1_df = option1_df.drop_duplicates(subset=['merged'])
option1_df = option1_df.rename(columns = {'MemberOfGroup':'MemberOfGroup1','IsFeatureOptional':'IsFeatureOptional1','IsDefault':'IsDefault1','ImageSmallURL_en-US':'ImageSmallURL_en-US1','Active':'Active1','CustomData':'CustomData1'})


# In[90]:


option2_df = option1_df[['merged','MemberOfGroup1','IsFeatureOptional1','IsDefault1']]


# In[91]:


option_df = option_df.merge(option2_df,how = 'left',on= 'merged')


# In[92]:


option_df.loc[option_df['MemberOfGroup1'] == 'StylePricing', 'MemberOfGroup'] = 'StylePricing'
option_df.loc[option_df['MemberOfGroup1'] == 'WorkTop', 'MemberOfGroup'] = 'WorkTop'
option_df.loc[option_df['IsFeatureOptional1']==1,'IsFeatureOptional'] = 'True'
option_df.loc[option_df['IsDefault1']==1,'IsDefault']= 'True'


# In[93]:


option3_df = option1_df[['merged','ImageSmallURL_en-US1','Active1','CustomData1']]


# In[94]:


option_df = option_df[['Code','Parent','IsGroup','Type','MemberOfGroup','Name_en-US','ShortDescription_en-US','Description_en-US','LongDescription_en-US','IsFeatureOptional','IsDefault','IsRepeatable','SetOptionOverride','AssetCode','ParamCode','MoreInfoURL_en-US','Icon_en-US','ImageSmallURL_en-US','ImageMediumURL_en-US','ImageLargeURL_en-US','DisplayOrder','Active','EffectiveDate','ExpirationDate','NumericValues','CustomData','Metadata[Option.HasGeometry]','Metadata[Option.HasMaterial]','SourceMaterialRef','merged',]]


# In[95]:


option_df = option_df.merge(option3_df,on='merged',how='left')


# In[96]:


option_df.loc[option_df['Active1']==0,'Active']='False'


# In[97]:


option_df.loc[option_df['CustomData1'].notna(),'CustomData'] = option_df['CustomData1']


# In[98]:


small = option_df['ImageSmallURL_en-US']==''
option_df.loc[small,'ImageSmallURL_en-US']=option_df.loc[small,'ImageSmallURL_en-US1']


# In[99]:


medium = option_df['ImageMediumURL_en-US']==''
option_df.loc[medium,'ImageMediumURL_en-US']=option_df.loc[medium,'ImageSmallURL_en-US1']


# In[100]:


large = option_df['ImageLargeURL_en-US']==''
option_df.loc[large,'ImageLargeURL_en-US']=option_df.loc[large,'ImageSmallURL_en-US1']


# In[101]:


option_df = option_df[['Code','Parent','IsGroup','Type','MemberOfGroup','Name_en-US','ShortDescription_en-US','Description_en-US','LongDescription_en-US','IsFeatureOptional','IsDefault','IsRepeatable','SetOptionOverride','AssetCode','ParamCode','MoreInfoURL_en-US','Icon_en-US','ImageSmallURL_en-US','ImageMediumURL_en-US','ImageLargeURL_en-US','DisplayOrder','Active','EffectiveDate','ExpirationDate','NumericValues','CustomData','Metadata[Option.HasGeometry]','Metadata[Option.HasMaterial]','SourceMaterialRef']]


# In[102]:


product_df = product_df.drop(product_df[product_df['Feature'].str.contains('825')].index)


# In[103]:


product_df = product_df.drop(product_df[product_df['Feature'].str.contains('826')].index)


# In[104]:


option_df.to_excel(Output_option_path,index = False)
product_df.to_excel(Output_pxf_path,index = False)


# In[ ]:




