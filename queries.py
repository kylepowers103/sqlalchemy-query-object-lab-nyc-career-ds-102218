from sqlalchemy import create_engine, func
from seed import Company
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///dow_jones.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

def return_apple():
    apple = session.query(Company).filter(Company.company=='Apple').first()
    return apple
    #for instance in session.query(User).order_by(User.id):
     #print(instance.name, instance.fullname)


def return_disneys_industry():
    disney = session.query(Company).filter(Company.company=='Walt Disney').first()
    return disney.industry

def return_list_of_company_objects_ordered_alphabetically_by_symbol():
    companies = session.query(Company).order_by(Company.symbol).all()
    return companies

def return_list_of_dicts_of_tech_company_names_and_their_EVs_ordered_by_EV_descending():
    tech = session.query(Company).filter_by(industry='Technology').order_by(Company.enterprise_value.desc())
    list = []
    for co in tech:
        obj = {'company': co.company, 'EV': co.enterprise_value}
        list.append(obj)
    return list

def return_list_of_consumer_products_companies_with_EV_above_225():
    list = []
    for company in session.query(Company).filter(Company.industry=='Consumer products', Company.enterprise_value>225).all():
        list.append({'name': company.company})
    return list

def return_conglomerates_and_pharmaceutical_companies():
    from sqlalchemy import or_
    list = []
    for company in session.query(Company).filter(or_(Company.industry=='Conglomerate', Company.industry=='Pharmaceuticals')):
        list.append(company.company)
    return list

def avg_EV_of_dow_companies():
    return session.query(func.avg(Company.enterprise_value)).first()

def return_industry_and_its_total_EV():
    return session.query(Company.industry, func.sum(Company.enterprise_value)).group_by(Company.industry).all()
