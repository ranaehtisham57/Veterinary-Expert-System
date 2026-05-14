import disease_diagnosis as dd
import doctors_assignment as doc
import pandas as pd
import prettytable as pt


def get_status(score):
    if score >= 2.0:
        return "High"
    elif score >= 1.0:
        return "Medium"
    else:
        return "Low"


def main():
    print()
    print("================ DIAGNOSIS Session ================")
    print()
    animal_type=input("Enter Your Animal Type = ")
    symptoms_input=input("Enter Symptoms (Comma Separated) = ")
    symptoms=[x.lower() for x in symptoms_input.split(',')]
    disease_diagnose=dd.create_object()
    doctors=doc.create_object()
    diseases=disease_diagnose.calculate_score(symtoms=symptoms)
    print("================ DIAGNOSIS REPORT ================")
    print()
    dis_table=pt.PrettyTable()
    dis_table.field_names=["Disease", "Score","Status"]
    for key,val in diseases.items():
        diseaase_status=get_status(val)
        dis_table.add_row([key,val,diseaase_status])

    print(dis_table)
    print()
    print("================ System Confidence ================")
    print()
    confidence_dict=disease_diagnose.calculate_confidence(diseases)
    conf_table=pt.PrettyTable()
    conf_table.field_names=["Status","Confidence"]
    for key,val in confidence_dict.items():
        conf_table.add_row([key,val])

    print(conf_table)

    print()
    print("==============TREATMENT (Top Disease)============")
    print()
    treatment_recommend=disease_diagnose.treatment_recommend(diseases)
    data = pd.DataFrame([treatment_recommend])
    print(data.to_string(index=False,col_space=13,justify='left'))
    print()
    print("==============RECOMMENDED DOCTORS============")
    print()
    choice=input("Do you want a recommendation for a doctor (yes/no) = ").lower()
    if choice=="yes":
        budget=int(input("Enter your budget = "))
        location=input("Enter Location for doctor = ").lower()
        recommended_doc=doctors.recommend_doctor(loc=location,price=budget)
        doc_table = pt.PrettyTable()

        doc_table.field_names = ["ID","Name", "City", "Specialty", "Fee", "Contact", "Email", "Score"]
        doc_table.max_width = 10
        doc_table.align = "l"

        for key, value in recommended_doc.items():
            doc_table.add_row([
                key,
                value[0][:18],
                value[1],
                value[2],
                value[3],
                value[4],
                value[5][:20],
                value[6]
            ])
        print()
        print("==============RECOMMENDED DOCTORS LIST============")
        print()
        print(doc_table)
    else:
        print("OK Take CARE YOUR ANIMAl!😊")


if __name__=="__main__":
    main()