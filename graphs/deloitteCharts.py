import numpy as np
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import seaborn as sns
plt.style.use('seaborn-deep')

df1 = pd.read_excel('../DDS9_Data_Extract_with_labels.xlsx')
df2 = pd.read_excel('../DDS10_Data_Extract_with_labels.xlsx')
df3 = pd.read_excel('../DDS11_Data_Extract_with_labels.xlsx')

# will need to change headers in document out for these to work. Each report varies a little in which columns are available too.
YesNoChoices = ['HasChildren', 'Children under 4', 'Children 5to9', 'Children 10to13', 'Children 14to18', 'Children 19to25', 'Children 26Up', 'Children Unknown',
                'HasFlatPanelTelevision', 'HasDVR', 'HasStreamingBox', 'HasThumbdrive', 'HasBluRay', 'HasGamingConsole', 'HasPortableGamingConsole', 'HasWirelessRouter',
                'HasDesktop', 'HasLaptop', 'HasLaptopHybrid', 'HasLargeTablet', 'HasSmallTablet', 'HasEReader', 'HasSmallSmartphone', 'HasLargeSmartphone', 'HasBasicPhone',
                'HasSmartWatch', 'HasFitnessBand', 'HasSmartGlasses', 'Has3dPrinter', 'HasNoDevices', 'HasUnknownDevices', 'PurchaseFlatPanelTelevision', 'PurchaseDVR',
                'PurchaseStreamingBox', 'PurchaseThumbdrive', 'PurchaseBluRay', 'PurchaseGamingConsole', 'PurchasePortableGamingConsole', 'PurchaseWirelessRouter',
                'PurchaseDesktop', 'PurchaseLaptop', 'PurchaseLaptopHybrid', 'PurchaseLargeTablet', 'PurchaseSmallTablet', 'PurchaseEReader',
                'PurchaseSmallSmartphone', 'PurchaseLargeSmartphone', 'PurchaseBasicPhone', 'PurchaseSmartWatch', 'PurchaseFitnessBand', 'PurchaseSmartGlasses',
                'Purchase3dPrinter', 'PurchaseNoDevices', 'PurchaseUnknownDevices', 'FrequentApp-Photo', 'FrequentApp-Banking', 'FrequentApp-Health', 'FrequentApp-Food',
                'FrequentApp-Retail', 'FrequentApp-Navigation', 'FrequentApp-SocialMedia', 'FrequentApp-Books', 'FrequentApp-Music', 'FrequentApp-VideoStreaming',
                'FrequentApp-Reviews', 'FrequentApp-News', 'FrequentApp-Newspaper', 'FrequentApp-Magazines', 'FrequentApp-Utilities', 'FrequentApp-QRReader',
                'FrequentApp-Travel', 'FrequentApp-Transport', 'FrequentApp-Location', 'FrequentApp-Language', 'FrequentApp-Movie', 'FrequentApp-Business',
                'FrequentApp-Games', 'FrequentApp-Productivity', 'FrequentApp-Sports', 'FrequentApp-Weather', 'FrequentApp-Browser', 'FrequentApp-VOIP', 'FrequentApp-None',
                'FrequentApp-Unknown']



uniqueChoices = ['Region', 'Employment Status', 'Ethnicity']

valueChoices = ['ValueFlatPanelTelevision', 'ValueDVR', 'ValueStreamingBox', 'ValueThumbDrive', 'ValueBlueRay', 'ValueGamingConsole',
                'ValuePortableGamingConsole', 'ValueNetworkRouter', 'ValueDesktop', 'ValueLaptop', 'ValueLaptopHybrid', 'ValueLargeTablet', 'ValueSmallTablet', 'ValueEReader',
                'ValueSmallSmartphone', 'ValueLargeSmartphone', 'ValueBasicPhone', 'ValueSmartWatch', 'ValueFitnessBand', 'ValueSmartGlasses', 'Value3dPrinter', 'ValuePlaceholder']

numericChoices = ["TimeWatchingMoviesSmartphone", "TimeWatchingMoviesTablet", "TimeWatchingMoviesPC", "TimeWatchingMoviesTV", "TimeWatchingSportsSmartphone", "TimeWatchingSportsTablet",
                  "TimeWatchingSportsPC", "TimeWatchingSportsTV", "TimeWatchingTvSmartphone", "TimeWatchingTvTablet", "TimeWatchingTvPC", "TimeWatchingTvTV"]


Ages1 = df1['Age']
Gender1 = df1['Gender']
Gender2 = df2['Gender']
Gender3 = df3['Gender']

df1.fillna(0, inplace=True)
df2.fillna(0, inplace=True)
df3.fillna(0, inplace=True)

# Gender Charts
Gender1.replace(['Female', 'Male'], [0, 1], inplace=True)
Gender2.replace(['Female', 'Male'], [0, 1], inplace=True)
Gender3.replace(['Female', 'Male'], [0, 1], inplace=True)

genderData = [Gender1, Gender2, Gender3]
plt.hist(genderData, bins = 2, histtype='bar', label=['Set 1', 'Set 2', 'Set 3'])
plt.legend(loc='upper right')
plt.title('Gender')
plt.xticks([0, 1], ['Female', 'Male'])
plt.show()

for item in uniqueChoices:
    currentItem1 = df1[item]
    currentItem2 = df2[item]
    currentItem3 = df3[item]
    uniqueChoices1 = np.sort(pd.unique(currentItem1))
    uniqueChoices2 = np.sort(pd.unique(currentItem3))
    uniqueChoices3 = np.sort(pd.unique(currentItem3))

    if(len(uniqueChoices1) > 1):
        numerics = np.arange(len(uniqueChoices1))
        currentItem1.replace(uniqueChoices1, numerics)
        currentItem2.replace(uniqueChoices2, numerics)
        currentItem3.replace(uniqueChoices3, numerics)

        print(currentItem2)

        itembins = len(uniqueChoices)

        dataChoices = [currentItem1, currentItem2, currentItem3]
        plt.hist(dataChoices, bins=itembins, histtype='bar')
        plt.title(item)
        plt.xticks(numerics, uniqueChoices, rotation='vertical', multialignment='center')
        plt.margins(0.2)
        plt.subplots_adjust(bottom=0.6)
        plt.show()


for item in numericChoices:
    numItem1 = df1[item]
    numItem2 = df2[item]
    numItem3 = df3[item]
    numData = [numItem1, numItem2, numItem3]
    plt.hist(numData, bins = 10, histtype='bar')
    plt.title(item)
    plt.margins(0.2)
    plt.subplots_adjust(bottom=0.6)
    plt.show()


for valQ in valueChoices:
    valueItem1 = df1[valQ]
    valueItem2 = df2[valQ]
    valueItem3 = df3[valQ]
    uniqueValueChoices = np.sort(pd.unique(valueItem1))

    if(len(uniqueValueChoices) > 1):
        valnumerics = np.arange(len(uniqueValueChoices))
        valueItem1.replace(uniqueValueChoices, valnumerics)
        valueItem2.replace(uniqueValueChoices, valnumerics)
        valueItem3.replace(uniqueValueChoices, valnumerics)
        itembins = len(uniqueValueChoices)

        valueData = [valueItem1, valueItem2, valueItem3]
        plt.hist(valueData, bins=itembins, histtype='bar')
        plt.title(valQ)
        plt.xticks(valnumerics, uniqueValueChoices, rotation='vertical', multialignment='center')
        plt.margins(0.2)
        plt.subplots_adjust(bottom=0.6)
        plt.show()


for choice in YesNoChoices:
    choiceItem1 = df1[choice]
    choiceItem2 = df2[choice]
    choiceItem3 = df3[choice]
    choiceItem1.replace(['No', 'Yes'], [1, 2], inplace=True)
    choiceItem2.replace(['No', 'Yes'], [1, 2], inplace=True)
    choiceItem3.replace(['No', 'Yes'], [1, 2], inplace=True)
    choiceData = [choiceItem1, choiceItem2, choiceItem3]

    plt.hist(choiceData, bins=3, histtype='bar', label=['Set 1', 'Set 2', 'Set 3'])
    plt.xlabel(choice)
    plt.xticks([0, 1, 2], ["No Answer", "No", "Yes"])
    plt.show()
