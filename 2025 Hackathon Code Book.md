## **2025 Hackathon Code Book**

## **Context**

Section 8 housing is a program funded by the United States Department of Housing and Urban Development to provide low income families, seniors, and people with disabilities with affordable housing. The department pays partial or all rent costs for eligible housing to ensure these individuals have safe and private housing. This data set focuses on section 8 housing information for the states within the Pacific Northwest from 2023\. Below are definitions of the columns in the data set provided.

## **Location identifiers**

* **state\_code**: Numerical code representing the state.  
* **county\_code**: Unique numerical identifier for the county within the state.  
* **county\_sub\_code**: Subdivision code for the county (99999 typically indicates entire county)  
* **state\_alpha**: Two-letter alphabetic state code.  
* **county\_name**: Name of the county.  
* **hud\_areaname**: The United States Department of Housing and Urban Development (HUD) defined cities. The Metropolitan Statistical Area (MSA) acronym is used to denote counties located in or adjacent to major cities.  
* **fips2010**: Full FIPS (Federal Information Processing Standard) code for the geographic area. These codes are used to make efficient and informed decisions on the county level (concatenation of **state\_code** and **county\_code** and **county\_sub\_code**).  
* **hud\_area\_code**: Unique code for the HUD area.

## **Rent Information (Fair Market Values)**

* **rent\_50\_0**: Median (middle point) of rent for a studio or 0-bedroom unit.  
* **rent\_50\_1**: Median rent for a 1-bedroom unit.  
* **rent\_50\_2**: Median rent for a 2-bedroom unit.  
* **rent\_50\_3**: Median rent for a 3-bedroom unit.  
* **rent\_50\_4**: Median rent for a 4-bedroom unit.

## **Additional data from Census Bureau (ACS-5, 2023\)**

* **GEOID**: Census Bureau geographic identifier of a state within the county (concatenation of **state\_code** and **county\_code**).  
* **median\_incomeE**: An estimate that represents the middle point of family income in a county.  
* **median\_incomeM**: The margin of error of the median income estimate.  
* **poverty\_popE**: An estimate of the number of residents within a county. living at the federal poverty level (determined by family income and number of members in a household).  
* **poverty\_popM**: The margin of error of the poverty population estimate.  
* **total\_popE**: An estimate of the total number of people living within the county listed.  
* **total\_popM**: The margin of error of the total population estimate.  
* **median\_rentE**: An estimate that represents the middle point of rent prices within a county.  
* **median\_rentM**: The margin of error of median rent costs.

## **Sources**

“2023 Federal Poverty Guidelines Announced.” My Benefit Advisor, 24 Jan. 2023, [www.mybenefitadvisor.com/siteassets/documents/2023/q1/2023-federal-poverty-guidelines-announced---012323m.pdf?v=48f89f](http://www.mybenefitadvisor.com/siteassets/documents/2023/q1/2023-federal-poverty-guidelines-announced---012323m.pdf?v=48f89f). 

Bibler, Adam. “50th Percentile Rent Estimates | HUD USER.” Www.huduser.gov, [www.huduser.gov/portal/datasets/50per.html\#year2023](http://www.huduser.gov/portal/datasets/50per.html#year2023). 

“Housing Choice Voucher (Section 8\) | USAGov.” Www.usa.gov, 2 Dec. 2024, [www.usa.gov/housing-voucher-section-8](http://www.usa.gov/housing-voucher-section-8). 