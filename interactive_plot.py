from bokeh.models import CustomJS, ColumnDataSource, Select
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Spectral11
from bokeh.layouts import column
import pandas as pd

data_file = "/Users/ocallaghang2/Desktop/Python_Github/Class_project/CBT_outpatient_2019.xlsx"
psych_data = pd.read_excel(data_file)
psych_data['Clinical_Visit_Date'] = pd.to_datetime(psych_data.Clinical_Visit_Date)

#%% Creating participant subsets 

ARLS2 = psych_data[psych_data.Initials == 'ARLS2']
KYME = psych_data[psych_data.Initials == 'KYME']
JEEA = psych_data[psych_data.Initials == 'JEEA']
RNMN = psych_data[psych_data.Initials == 'RNMN']
JNGN = psych_data[psych_data.Initials == 'JNGN']
LESG = psych_data[psych_data.Initials == 'LESG']
CEKY = psych_data[psych_data.Initials == 'CEKY']
ANQS = psych_data[psych_data.Initials == 'ANQS']
KALT = psych_data[psych_data.Initials == 'KALT']
DDKL = psych_data[psych_data.Initials == 'DDKL']
LAGN = psych_data[psych_data.Initials == 'LAGN']
JEJS = psych_data[psych_data.Initials == 'JEJS']
DOWS = psych_data[psych_data.Initials == 'DOWS']

# participant_list = ['ARLS2', 'KYME', 'JEEA', 'RNMN', 'JNGN', 'LESG', 'CEKY', 'ANQS', 'KALT', 'DDKL', 'LAGN', 'JEJS', 'DOWS']
# def get_data(name):
#     df = psych_data[psych_data.Initials == name]
#     return ColumnDataSource(data=df)

#%%
p = figure(width=1000, height=500, x_axis_type="datetime", y_range=[0, 27])

r_ARLS2 = p.multi_line(xs=[ARLS2.Clinical_Visit_Date.values]*2, ys=[ARLS2.s_mfq_tot.values, ARLS2.p_mfq_tot.values], color=['red','green'])
r_KYME = p.multi_line(xs=[KYME.Clinical_Visit_Date.values]*2, ys=[KYME.s_mfq_tot.values, KYME.p_mfq_tot.values], color=['red','green'])
r_JEEA = p.multi_line(xs=[JEEA.Clinical_Visit_Date.values]*2, ys=[JEEA.s_mfq_tot.values, JEEA.p_mfq_tot.values], color=['red','green'])
r_RNMN = p.multi_line(xs=[RNMN.Clinical_Visit_Date.values]*2, ys=[RNMN.s_mfq_tot.values, RNMN.p_mfq_tot.values], color=['red','green'])
r_JNGN = p.multi_line(xs=[JNGN.Clinical_Visit_Date.values]*2, ys=[JNGN.s_mfq_tot.values, JNGN.p_mfq_tot.values], color=['red','green'])
r_LESG = p.multi_line(xs=[LESG.Clinical_Visit_Date.values]*2, ys=[LESG.s_mfq_tot.values, LESG.p_mfq_tot.values], color=['red','green'])
r_CEKY = p.multi_line(xs=[CEKY.Clinical_Visit_Date.values]*2, ys=[CEKY.s_mfq_tot.values, CEKY.p_mfq_tot.values], color=['red','green'])
r_ANQS = p.multi_line(xs=[ANQS.Clinical_Visit_Date.values]*2, ys=[ANQS.s_mfq_tot.values, ANQS.p_mfq_tot.values], color=['red','green'])
r_KALT = p.multi_line(xs=[KALT.Clinical_Visit_Date.values]*2, ys=[KALT.s_mfq_tot.values, KALT.p_mfq_tot.values], color=['red','green'])
r_DDKL = p.multi_line(xs=[DDKL.Clinical_Visit_Date.values]*2, ys=[DDKL.s_mfq_tot.values, DDKL.p_mfq_tot.values], color=['red','green'])
r_LAGN = p.multi_line(xs=[LAGN.Clinical_Visit_Date.values]*2, ys=[LAGN.s_mfq_tot.values, LAGN.p_mfq_tot.values], color=['red','green'])
r_JEJS = p.multi_line(xs=[JEJS.Clinical_Visit_Date.values]*2, ys=[JEJS.s_mfq_tot.values, JEJS.p_mfq_tot.values], color=['red','green'])
r_DOWS = p.multi_line(xs=[DOWS.Clinical_Visit_Date.values]*2, ys=[DOWS.s_mfq_tot.values, DOWS.p_mfq_tot.values], color=['red','green'])

#%% All particioants are included in plot but hidden until they are selected by the dropdown 
callback = CustomJS(args=dict(r_ARLS2=r_ARLS2, r_KYME=r_KYME, r_JEEA=r_JEEA, r_RNMN=r_RNMN, r_JNGN=r_JNGN, r_LESG=r_LESG, r_CEKY=r_CEKY, r_ANQS=r_ANQS, r_KALT=r_KALT, r_DDKL=r_DDKL, r_LAGN=r_LAGN, r_JEJS=r_JEJS, r_DOWS=r_DOWS), code="""
    f = cb_obj.value;
    r_ARLS2.visible = false;
    r_KYME.visible = false;
    r_JEEA.visible = false;
    r_RNMN.visible = false;
    r_JNGN.visible = false;
    r_LESG.visible = false;
    r_CEKY.visible = false;
    r_ANQS.visible = false;
    r_KALT.visible = false;
    r_DDKL.visible = false;
    r_LAGN.visible = false;
    r_JEJS.visible = false;
    r_DOWS.visible = false;
    if      (f == "ARLS2") { r_ARLS2.visible = true; }
    else if (f == "KYME") { r_KYME.visible = true; }
    else if (f == "JEEA")  { r_JEEA.visible = true; }
    else if (f == "RNMN")  { r_RNMN.visible = true; }
    else if (f == "JNGN")  { r_JNGN.visible = true; }
    else if (f == "LESG")  { r_LESG.visible = true; }
    else if (f == "CEKY")  { r_CEKY.visible = true; }
    else if (f == "ANQS")  { r_ANQS.visible = true; }
    else if (f == "KALT")  { r_KALT.visible = true; }
    else if (f == "DDKL")  { r_DDKL.visible = true; }
    else if (f == "LAGN")  { r_LAGN.visible = true; }
    else if (f == "JEJS")  { r_JEJS.visible = true; }
    else if (f == "DOWS")  { r_DOWS.visible = true; }
    else {
        r_ARLS2.visible = true;
        r_KYME.visible = true;
        r_JEEA.visible = true;
        r_RNMN.visible = true;
        r_JNGN.visible = true;
        r_LESG.visible = true;
        r_CEKY.visible = true;
        r_ANQS.visible = true;
        r_KALT.visible = true;
        r_DDKL.visible = true;
        r_LAGN.visible = true;
        r_JEJS.visible = true;
        r_DOWS.visible = true;
    }
""")

#%%
participants = ["ARLS2", "KYME", "JEEA", "RNMN", "JNGN", "LESG", "CEKY", "ANQS", "KALT", "DDKL", "LAGN", "JEJS", "DOWS", 'All']
multi_select = Select(title="Select Participant:", value=participants[13], options=participants, callback=callback)

output_file("CBT_plot.html")

show(column(multi_select, p))