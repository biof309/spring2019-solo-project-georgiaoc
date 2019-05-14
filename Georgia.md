# Georgia O'Callaghan

- Postdoc @ MBDU, NIMH

# Project aim

- CBT outpatient program
- Clinician progress review

# Process

- Package review
- Issues to resolve

# The code 

- Sample for two participants: 

    ```python
    p = figure(width=1000, height=500, x_axis_type="datetime", y_range=[0, 27])

    r_ARLS2 = p.multi_line(xs=[ARLS2.Clinical_Visit_Date.values]*2, ys=[ARLS2.s_mfq_tot.values, ARLS2.p_mfq_tot.values], color=['red','green'])
    r_KYME = p.multi_line(xs=[KYME.Clinical_Visit_Date.values]*2, ys=[KYME.s_mfq_tot.values, KYME.p_mfq_tot.values], color=['red','green'])

    callback = CustomJS(args=dict(r_ARLS2=r_ARLS2, r_KYME=r_KYME), code="""
        f = cb_obj.value;
        r_ARLS2.visible = false;
        r_KYME.visible = false;
        if      (f == "ARLS2") { r_ARLS2.visible = true; }
        else if (f == "KYME") { r_KYME.visible = true; }
        }
    """)

    participants = ["ARLS2", "KYME", 'All']
    multi_select = Select(title="Select Participant:", value=participants[2], options=participants, callback=callback)

    output_file("CBT_plot.html")
    show(column(multi_select, p))
    ```

# Result 

- [Demo graph](https://georgiaoc.github.io/biof309_assignment/CBT_plot.html)

# What I learnt

- Failures/problems
- Take away 

# The end 

- Thanks to Martin, Jinping, Michael & Nick!
- Questions? 
