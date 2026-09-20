# A/B Testing

A marketing campaign targeting website users was conducted with the aim of increasing product sales. To this end, an advertisement was specifically developed for this purpose.

To determine whether the campaign succeeded in its objective, specifically, whether the ad actually contributed to driving more sales, website users were randomly selected and divided into two groups: one group that saw the specifically designed ad (AD) and a control group that was shown a generic ad (PSA).

Our goal here is **to verify whether the conversion rate of the AD group is higher than that of the control group (PSA) and whether the observed difference is statistically significant**.

The analysis was performed using the [Marketing A/B Testing](https://www.kaggle.com/datasets/faviovaz/marketing-ab-testing) dataset, which involves an A/B test: _"a randomized experiment in which different versions of a variable (such as an advertisement or system features) are presented to different groups of users simultaneously. The objective is to evaluate the impact of the variable on the final outcome."_

## Resultados

- Just over 588,000 users were analyzed and divided into two groups: one exposed to an ad specifically designed to sell a product (AD) and another serving as a control, exposed to a generic ad (PSA).
- It was observed that users exposed to the specific ad (AD) had a conversion rate 43% higher than those in the control group (PSA): p_AD = 2.55% versus p_PSA = 1.79%.
- Testing confirmed that this difference in conversion rates is statistically significant, meaning it is not merely statistical noise.
- We observed that the conversion rate increases alongside the number of ads viewed by users, reaching nearly 17% when users are exposed to more than 100 ads.
- We also determined that the days of the week with the highest conversion rates are Monday and Tuesday, and the optimal time window for displaying ads is between 2:00 PM and 9:00 PM.
