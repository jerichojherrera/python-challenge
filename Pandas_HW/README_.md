

```python
#Obervable Trend 1: Based on gender, there are dominantly male players

#Observable Trend 2: Based on age, the players are dominantly 20-24 year olds

#Observable Trend 3: There is barely anyone 40 years of age or older that plays this game (less than 3%)
```


```python
import pandas as pd
import os
import numpy as np
```


```python
purchase_data_df = pd.read_json("purchase_data.json")
purchase_data_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Age</th>
      <th>Gender</th>
      <th>Item ID</th>
      <th>Item Name</th>
      <th>Price</th>
      <th>SN</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>38</td>
      <td>Male</td>
      <td>165</td>
      <td>Bone Crushing Silver Skewer</td>
      <td>$3.37</td>
      <td>Aelalis34</td>
    </tr>
    <tr>
      <th>1</th>
      <td>21</td>
      <td>Male</td>
      <td>119</td>
      <td>Stormbringer, Dark Blade of Ending Misery</td>
      <td>$2.32</td>
      <td>Eolo46</td>
    </tr>
    <tr>
      <th>2</th>
      <td>34</td>
      <td>Male</td>
      <td>174</td>
      <td>Primitive Blade</td>
      <td>$2.46</td>
      <td>Assastnya25</td>
    </tr>
    <tr>
      <th>3</th>
      <td>21</td>
      <td>Male</td>
      <td>92</td>
      <td>Final Critic</td>
      <td>$1.36</td>
      <td>Pheusrical25</td>
    </tr>
    <tr>
      <th>4</th>
      <td>23</td>
      <td>Male</td>
      <td>63</td>
      <td>Stormfury Mace</td>
      <td>$1.27</td>
      <td>Aela59</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Player Count

#Total Number of Players
total_players = purchase_data_df["Age"].count()
```


```python
#Total Number of Players (Final):
player_count_summary = pd.DataFrame({"Total Number of Players": [total_players]})
player_count_summary
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Number of Players</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>780</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchase Analysis (Total)

#Total Number of unique items
unique = purchase_data_df["Item Name"].nunique()
```


```python
#Avg. Purchase Price
avg_purchase_price = purchase_data_df["Price"].mean()
```


```python
def round2(number):
    rounded_number = round(number, 2)
    string = str(rounded_number)
    return string
avg_purchase_price2 = "$"+(round2(avg_purchase_price))
```


```python
#Total Number of Purchases
total_purchases = purchase_data_df["SN"].count()
```


```python
#Total Revenue
total_revenue = purchase_data_df["Price"].sum()
```


```python
total_revenue2 = "$"+(round2(total_revenue))
```


```python
purchasing_analysis_total = pd.DataFrame({"Total Number of Unique Items": [unique],
                              "Average Purchase Price": [(avg_purchase_price2)],
                              "Total Number of Purchases": [total_purchases],
                              "Total Revenue": [total_revenue2]})
```


```python
#Purchase Analysis (Total) [Final]:
organized_purchase_analysis = purchasing_analysis_total[["Total Number of Unique Items", 
                                                         "Average Purchase Price", 
                                                         "Total Number of Purchases", 
                                                         "Total Revenue"]]
organized_purchase_analysis
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Number of Unique Items</th>
      <th>Average Purchase Price</th>
      <th>Total Number of Purchases</th>
      <th>Total Revenue</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>179</td>
      <td>$2.93</td>
      <td>780</td>
      <td>$2286.33</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Gender Demographics:

#Percentage and Count of Male Players
genders = purchase_data_df["Gender"].value_counts()
```


```python
gender_percent = (genders/total_players)*100
pd.options.display.float_format = '{:,.2f}%'.format
```


```python
gender_demographics = pd.concat([gender_percent,genders], axis=1)
```


```python
#Gender Demographics (Final):
gender_demographics.columns=['Percentage of Players','Total Count']
gender_demographics
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Male</th>
      <td>81.15%</td>
      <td>633</td>
    </tr>
    <tr>
      <th>Female</th>
      <td>17.44%</td>
      <td>136</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>1.41%</td>
      <td>11</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Purchasing Analysis (Gender)

gender_group = purchase_data_df.groupby('Gender')
gender_avg_purchases = gender_group['Price'].mean()
pd.options.display.float_format = '${:,.2f}'.format
```


```python
gender_total_purchase_value = gender_group['Price'].sum()
pd.options.display.float_format = '${:,.2f}'.format
```


```python
normalized_totals = gender_avg_purchases
```


```python
#Purchasing Analysis (Gender) [Final]:

gender_purchase_analysis_final = pd.concat([genders,gender_avg_purchases,
                                            gender_total_purchase_value,
                                            normalized_totals], axis=1)
```


```python
gender_purchase_analysis_final.columns=['Purchase Count',
                                        'Average Purchase Price',
                                        'Total Purchase Price',
                                        'Normalized Totals']
gender_purchase_analysis_final
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Price</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Female</th>
      <td>136</td>
      <td>$2.82</td>
      <td>$382.91</td>
      <td>$2.82</td>
    </tr>
    <tr>
      <th>Male</th>
      <td>633</td>
      <td>$2.95</td>
      <td>$1,867.68</td>
      <td>$2.95</td>
    </tr>
    <tr>
      <th>Other / Non-Disclosed</th>
      <td>11</td>
      <td>$3.25</td>
      <td>$35.74</td>
      <td>$3.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Age Demographics

bins = [0,10,14,19,24,29,34,39,100]
group_names = ['<10','10-14','15-19','20-24','25-29','30-34','34-39','40+']
age_demo = pd.cut(purchase_data_df['Age'], bins, labels=group_names)
age_demo_counts = age_demo.value_counts()
```


```python
age_count_df = pd.DataFrame({"Total Counts": age_demo_counts})
```


```python
age_percent = (age_demo_counts/total_players)*100
pd.options.display.float_format = '{:,.2f}%'.format
```


```python
#Age Demo (% and Total Count)[Final]:

age_count_and_percent = pd.concat([age_percent,age_demo_counts], axis=1)
```


```python
age_count_and_percent.columns=['Percentage of Players','Total Count']
```


```python
age_count_and_percent.reindex(["<10","10-14","15-19","20-24","25-29","30-34","34-39","40+"])
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Percentage of Players</th>
      <th>Total Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>&lt;10</th>
      <td>4.10%</td>
      <td>32</td>
    </tr>
    <tr>
      <th>10-14</th>
      <td>3.97%</td>
      <td>31</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>17.05%</td>
      <td>133</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>43.08%</td>
      <td>336</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>16.03%</td>
      <td>125</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>8.21%</td>
      <td>64</td>
    </tr>
    <tr>
      <th>34-39</th>
      <td>5.38%</td>
      <td>42</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>2.18%</td>
      <td>17</td>
    </tr>
  </tbody>
</table>
</div>




```python
purchase_data_df["Age Group"] = pd.cut(purchase_data_df['Age'], bins, labels=group_names)
pd.options.display.float_format = '{:,.2f}'.format
```


```python
age_avg_price = purchase_data_df.groupby("Age Group")
pd.options.display.float_format = '${:,.2f}'.format
age_average_final = age_avg_price['Price'].mean()
```


```python
age_total_price = purchase_data_df.groupby("Age Group")
age_total_price_final = age_total_price['Price'].sum()
```


```python
age_normalized = age_average_final
```


```python
#Purchase Analysis (age)[Final]:
age_purchase_analysis_final = pd.concat([age_demo_counts, age_average_final, 
                                         age_total_price_final, age_normalized], axis=1)
```


```python
age_purchase_analysis_final.columns=['Purchase Count',
                                     'Average Purchase Price',
                                     'Total Purchase Price',
                                     'Normalized Totals']
age_purchase_analysis_final
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Purchase Count</th>
      <th>Average Purchase Price</th>
      <th>Total Purchase Price</th>
      <th>Normalized Totals</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10-14</th>
      <td>31</td>
      <td>$2.70</td>
      <td>$83.79</td>
      <td>$2.70</td>
    </tr>
    <tr>
      <th>15-19</th>
      <td>133</td>
      <td>$2.91</td>
      <td>$386.42</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>20-24</th>
      <td>336</td>
      <td>$2.91</td>
      <td>$978.77</td>
      <td>$2.91</td>
    </tr>
    <tr>
      <th>25-29</th>
      <td>125</td>
      <td>$2.96</td>
      <td>$370.33</td>
      <td>$2.96</td>
    </tr>
    <tr>
      <th>30-34</th>
      <td>64</td>
      <td>$3.08</td>
      <td>$197.25</td>
      <td>$3.08</td>
    </tr>
    <tr>
      <th>34-39</th>
      <td>42</td>
      <td>$2.84</td>
      <td>$119.40</td>
      <td>$2.84</td>
    </tr>
    <tr>
      <th>40+</th>
      <td>17</td>
      <td>$3.16</td>
      <td>$53.75</td>
      <td>$3.16</td>
    </tr>
    <tr>
      <th>&lt;10</th>
      <td>32</td>
      <td>$3.02</td>
      <td>$96.62</td>
      <td>$3.02</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Top Spenders
top_5_spenders_count = purchase_data_df['SN'].value_counts()
top_5_spenders_count.head()
```




    Undirrala66    5
    Hailaphos89    4
    Mindimnya67    4
    Saedue76       4
    Qarwen67       4
    Name: SN, dtype: int64




```python
top_5 = purchase_data_df.groupby("SN")
top_5_total = top_5['Price'].sum()
top_5_highest_total = top_5_total.sort_values(ascending=False).head()
```


```python
top_5_sn_df = pd.concat([top_5_highest_total],axis=1)
top_5_sn_df.columns = ['Total Purchase Value']
top_5_sn_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>SN</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Undirrala66</th>
      <td>$17.06</td>
    </tr>
    <tr>
      <th>Saedue76</th>
      <td>$13.56</td>
    </tr>
    <tr>
      <th>Mindimnya67</th>
      <td>$12.74</td>
    </tr>
    <tr>
      <th>Haellysu29</th>
      <td>$12.73</td>
    </tr>
    <tr>
      <th>Eoda93</th>
      <td>$11.58</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Popular Items
purchase_item_counts = purchase_data_df['Item Name'].value_counts()
top_5_purchases = purchase_item_counts.head()
```


```python
popular_df = pd.concat([top_5_purchases],axis=1)
popular_df.columns=['Item Count']
popular_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Item Count</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Final Critic</th>
      <td>14</td>
    </tr>
    <tr>
      <th>Betrayal, Whisper of Grieving Widows</th>
      <td>11</td>
    </tr>
    <tr>
      <th>Arcane Gem</th>
      <td>11</td>
    </tr>
    <tr>
      <th>Stormcaller</th>
      <td>10</td>
    </tr>
    <tr>
      <th>Serenity</th>
      <td>9</td>
    </tr>
  </tbody>
</table>
</div>




```python
#Most Profitable Items
top_5_item_profit = purchase_data_df.groupby("Item Name")
top_5_item_profit_total = top_5_item_profit['Price'].sum()
top_5_profitable_items_total = top_5_item_profit_total.sort_values(ascending=False).head()
```


```python
profitable_items = pd.concat([top_5_profitable_items_total], axis=1)
profitable_items.columns=['Total Purchase Value']
profitable_items
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Purchase Value</th>
    </tr>
    <tr>
      <th>Item Name</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>Final Critic</th>
      <td>$38.60</td>
    </tr>
    <tr>
      <th>Retribution Axe</th>
      <td>$37.26</td>
    </tr>
    <tr>
      <th>Stormcaller</th>
      <td>$34.65</td>
    </tr>
    <tr>
      <th>Spectral Diamond Doomblade</th>
      <td>$29.75</td>
    </tr>
    <tr>
      <th>Orenmir</th>
      <td>$29.70</td>
    </tr>
  </tbody>
</table>
</div>


