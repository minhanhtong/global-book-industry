import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

st.set_page_config(
    page_title="Global Book Industry",
    page_icon="📚",
    layout="wide"
)

st.sidebar.title("Navigation")
st.sidebar.write("Global Book Industry")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Go to",
    [
        "Introduction",
        "Plot 1: Global Distribution of Annual Books Read and Top 10 Countries by Books Read Per Year",
        "Plot 2: Top 10 Highest GDP Countries",
        "Plot 3: Global Book Sales by Format",
        "Plot 4: Percentage of E-Book and Printed Book Purchases by Country (2020)",
        "Plot 5: Reason why people buy books",
        "Plot 6: Top 10 Best-selling Genres",
        "Plot 7: Distribution of Weekly Reading Time by Book Genre",
        "Plot 8: Top 10 Most Rated Books",
        "Plot 9: Top 10 Authors by Number of Books",
        "Plot 10: Distribution of Author Ratings: Fiction vs. Non-fiction",
        "Conclusion"
    ]
)

st.title("GLOBAL BOOK INDUSTRY")
if page == "Introduction":

    st.header("Introduction")

    st.write("""
    The global book publishing industry remains an essential part of the cultural and knowledge economy, 
    continuously evolving alongside technological advancements and changing consumer behaviors. 
    In recent years, the rise of digital platforms, changing reading habits,
    and economic disparities across countries have significantly influenced how books are produced,
    distributed, and consumed worldwide.
    """)
    

if page == "Conclusion":
    st.header("Conclusion")

    st.write("""
    In conclusion, the global book industry landscape is diverse. It is necessary 
    for publishers to identify which factors to consider when strengthening sales strategies. 
    Our project delved into 4 main components of business planning and strategies: market evaluation, 
    customer analysis, product line and product quality management, and partnership consideration.
    The factors evaluated are: geography, economic power, book formats, purchase motivations, genres, 
    and authors to discover meaningful patterns and relationships that impact the global book industry landscape. 
    The analysis of data visualization suggested that when developing products and implementing sales strategies,
    multiple factors should be considered to dispel misconceptions and minimize inefficiency. 
    Hopefully, this project is useful for both academic study and practical decision-making in the book industry.
    """)

if page == "Plot 1: Global Distribution of Annual Books Read and Top 10 Countries by Books Read Per Year":

    st.header("Global Distribution of Annual Books Read")

    df = pd.read_csv("average-books-read-per-year-by-country-2026.csv")
    df = df.rename(columns={
    "BooksReadAnnually_2024": "Books Read Per Year"
})

    fig = px.choropleth(
        df,
        locations="country",
        locationmode="country names",
        color="Books Read Per Year",
        hover_name="country",
        color_continuous_scale=["yellow", "red"],
        title="Global Annual Books Read Distribution"
    )
    
    st.markdown("""
    The visualizations reveal how annual books read vary across surveyed countries. 
    As illustrated by the map, Europe is distinguished by its consistently high number 
    of annual books read with numerous countries reading 9 to 15 such as the UK, France 
    and Italy. Be that as it may, on average, North America dominate the number of books 
    read per year, which is mainly driven by the United State with 17 books read per year.

    In contrast, people in Africa read the fewest books each year. Following this, 
    South America and Oceania show a moderate reading level. Besides, a mixed picture 
    is recorded in Asia. While India ranks second among the top readers, other Asian 
    countries show much lower figures.

    The map and bar chart analysis reflect an uneven distribution of annual books read 
    and reading interest across continents. It is suggested that North America and Europe 
    are key customer segments with the strongest book read engagement. These continents 
    open the door for book publishers to grow and maximize profits. Nevertheless, it might 
    be risky for the book publishers to expand their market in Africa due to its low 
    book read interest.
    """)

    st.plotly_chart(fig)

    st.header("Top 10 Countries by Books Read Per Year")

    df = pd.read_csv("average-books-read-per-year-by-country-2026.csv")

    df.columns = df.columns.str.strip()

    df = df.rename(columns={
        "BooksReadAnnually_2024": "Books Per Year"
    })
    
    top10 = df.sort_values(
        by="Books Per Year",
        ascending=False
    ).head(10)

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.barplot(
        data=top10,
        x="Books Per Year",
        y="country",
        palette="Set3",
        ax=ax
    )

    for i, value in enumerate(top10["Books Per Year"]):

        ax.text(
            value + 0.1,
            i,
            str(value),
            va="center"
        )

    ax.set_title(
        "Top 10 Countries by Books Read Per Year",
        fontsize=16,
        fontweight="bold"
    )

    ax.set_xlabel("Books Read Per Year")
    ax.set_ylabel("")

    st.pyplot(fig)
    
if page == "Plot 2: Top 10 Highest GDP Countries":

    st.title("Top 10 Highest GDP Countries")

    df = pd.read_csv("GDP(constant dollars).csv")

    top10 = df.sort_values(
        by="GDP(constant dollars)",
        ascending=False
    ).head(10)

    fig, ax1 = plt.subplots(figsize=(12, 6))

    ax1.bar(
        top10["Country"],
        top10["GDP(constant dollars)"] / 1e3,
        color=[
            "#CDB4DB",  # pastel tím
            "#FFC8DD",  # pastel hồng
            "#BDE0FE",  # pastel xanh
            "#A2D2FF",  # pastel xanh trời
            "#E0BBE4",  # tím lavender
            "#FDCBDF",  # hồng nhạt
            "#CDE7FF",  # xanh icy
            "#D7C6F5",  # tím soft
            "#B5EAD7",  # xanh mint pastel
            "#FFDAEC"   # hồng pastel sáng
        ]
    )

    ax1.set_ylabel(
        "GDP (Billion $)",
        color="#9D4EDD",
        fontsize=12
    )

    plt.xticks(
        rotation=45
    )

    ax2 = ax1.twinx()

    ax2.plot(
        top10["Country"],
        top10["GDP(constant dollars)"],
        color="#C77DFF",
        linewidth=3,
        marker='o',
        markersize=8
    )

    ax2.scatter(
        top10["Country"],
        top10["GDP(constant dollars)"],
        color="#A2D2FF",
        s=120,
        edgecolors="white"
    )

    ax2.set_ylabel(
        "Books Read Per Year",
        color="#C77DFF",
        fontsize=12
    )

    plt.title(
        "Do Top 10 Highest GDP Countries Read More?",
        fontsize=16,
        fontweight='bold',
        color="#7B2CBF"
    )

    ax1.grid(
        alpha=0.25,
        linestyle='--'
    )

    ax1.set_facecolor("#FAF7FF")

    fig.patch.set_facecolor("#FAF7FF")

    st.pyplot(fig)
    st.markdown("""
    The mixed chart reveals limited evidence for a positive correlation between 
    higher-GDP countries and the number of books read annually. In some wealthy 
    nations, such as the United States and the United Kingdom, higher GDP is truly 
    associated with higher reading levels. Statistically, Americans and Britons 
    read 17 and 15 books each year, respectively.

    However, this relationship is not consistent across all ten wealthiest countries. 
    In fact, the other high GDP nations demonstrate a strong contradiction. Despite 
    being one of the top GDP countries, China’s yearly book reading level is relatively 
    low, numbering only 6.61 books each year. The same patterns can also be observed 
    in Germany and Japan.

    Therefore, economic wealth is not a determinant or a reliable indicator for book 
    publishers to evaluate customer and market potential.
    """)
    
if page == "Plot 3: Global Book Sales by Format":

    st.title("Global Book Sales by Format")

    data = {
        'Year': [2017, 2018, 2019, 2020, 2021, 2022, 2023, 2027],
        'Print': [71.50, 73.07, 72.55, 65.93, 70.71, 62.94, 64.35, 67.14],
        'Ebooks': [11.33, 12.14, 12.68, 12.79, 13.99, 13.20, 13.72, 15.29],
        'Audio': [0, 0, 0, 0, 4.85, 5.00, 5.16, 5.83]
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.stackplot(
        df['Year'],
        df['Print'],
        df['Ebooks'],
        df['Audio'],
        labels=['Print', 'Ebooks', 'Audio'],
        colors=[
            '#FFF3B0',
            '#B5EAD7',
            '#A2D2FF'
        ],
        alpha=0.9
    )

    ax.set_title(
        "Global Book Sales by Format",
        fontsize=16,
        fontweight='bold',
        color="#5E6472"
    )

    ax.set_xlabel(
        "Year",
        fontsize=12,
        color="#5E6472"
    )

    ax.set_ylabel(
        "Sales ($ Billion)",
        fontsize=12,
        color="#5E6472"
    )

    ax.legend(
        loc='upper left',
        fontsize=10
    )

    ax.grid(
        alpha=0.3,
        linestyle='--'
    )

    ax.set_facecolor("#FFFDF8")

    fig.patch.set_facecolor("#FFFDF8")

    st.pyplot(fig)
    st.markdown("""
The chart presents global book sales by format from 2017 to 2027, measured in billions of US dollars.

In 2017, printed book sales reached approximately 71.5 billion dollars, which was substantially higher than e-book sales at around 11.3 billion dollars.

Print sales rose slightly to about 73.1 billion dollars in 2018 before declining to roughly 65.9 billion dollars in 2020.

However, the market showed signs of recovery afterward, with printed book sales increasing again to around 70.7 billion dollars in 2021 and stabilizing at approximately 67.1 billion dollars by 2027.

E-book sales exhibit a steady upward trend over the observed period. Starting at approximately 11.3 billion dollars in 2017, e-book revenue gradually increases and is projected to reach about 15.3 billion dollars by 2027.

Audiobooks represent the fastest-growing segment among the three formats. First appearing significantly in the data around 2021 with sales of approximately 4.85 billion dollars, and continuing to rise steadily, reaching an estimated 5.83 billion dollars by 2027.
""")
    
    
if page == "Plot 5: Reason why people buy books":

    st.title("Reason why people buy books")

    data = {
        'Reason': [
            "Entertainment/leisure",
            "Gifts",
            "Other",
            "Self-improvement",
            "Work or school"
        ],
        'All reasons': [82.9, 21.2, 2.0, 41.4, 18.4],
        'Main reason': [50.1, 12.8, 1.0, 25.0, 11.1]
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots(figsize=(10, 6))

    y = range(len(df))

    ax.barh(
        y,
        df['All reasons'],
        color="#BDE0FE",
        label='All reasons'
    )

    ax.barh(
        y,
        df['Main reason'],
        color="#CDB4DB",
        label='Main reason'
    )

    ax.set_yticks(y)

    ax.set_yticklabels(
        df['Reason'],
        fontsize=11,
        color="#5E548E"
    )

    ax.set_xlabel(
        "Percentage (%)",
        fontsize=12,
        color="#5E548E"
    )

    ax.set_title(
        "Reasons Why People Buy Books",
        fontsize=16,
        fontweight='bold',
        color="#6D597A"
    )

    ax.legend(
        fontsize=10
    )

    ax.grid(
        axis='x',
        linestyle='--',
        alpha=0.25
    )

    ax.set_facecolor("#FAF7FF")

    fig.patch.set_facecolor("#FAF7FF")

    st.pyplot(fig)
    
    st.write("""
The chart illustrates the percentages of different reasons why people buy books, categorized into all reasons and main reasons.

Overall, entertainment and leisure is the most significant reason for purchasing books, while other reasons such as work or school and miscellaneous purposes account for much smaller proportions.

In detail, entertainment and leisure dominates the chart, accounting for approximately 82.9% of all reasons and 50.1% as the main reason. This indicates that reading is primarily viewed as a recreational activity. Self-improvement ranks second, with 41.4% for all reasons and 25.0% as the main reason, suggesting that personal development is also an important motivation.

Other categories, including gifts and work or school contribute moderately with values ranging between approximately 11% and 21%. In contrast, the other category represents a minimal proportion, which stand at only 2.0% for all reasons and 1.0% as the main reason.
""")

if page == "Plot 4: Percentage of E-Book and Printed Book Purchases by Country (2020)":

    st.title("Percentage of E-Book and Printed Book Purchases by Country (2020)")

    df = pd.DataFrame({

        "Country": [
            "China",
            "United States",
            "United Kingdom",
            "Japan",
            "South Korea",
            "Australia",
            "Spain",
            "Germany",
            "France",
            "India"
        ],

        "EBook": [
            24.4,
            22.7,
            20.0,
            17.3,
            16.8,
            15.9,
            14.3,
            10.4,
            7.5,
            5.6
        ],

        "PrintedBook": [
            32.0,
            44.5,
            48.7,
            40.1,
            34.6,
            41.2,
            49.3,
            58.0,
            52.1,
            24.5
        ]

    })

    fig, ax = plt.subplots(figsize=(11, 6))

    y = np.arange(len(df))

    bar_height = 0.35

    ax.barh(
        y - bar_height/2,
        df["EBook"],
        height=bar_height,
        label="E-Book",
        color="#66bb6a"
    )

    ax.barh(
        y + bar_height/2,
        df["PrintedBook"],
        height=bar_height,
        label="Printed Book",
        color="#c8e6c9"
    )

    for i in range(len(df)):

        ax.text(
            df["EBook"][i] + 0.5,
            y[i] - bar_height/2,
            f"{df['EBook'][i]}%",
            va="center"
        )

        ax.text(
            df["PrintedBook"][i] + 0.5,
            y[i] + bar_height/2,
            f"{df['PrintedBook'][i]}%",
            va="center"
        )

    ax.set_yticks(y)

    ax.set_yticklabels(df["Country"])

    # X axis limit
    ax.set_xlim(0, 65)

    ax.set_title(
        "E-Books Still No Match for Printed Books",
        fontsize=16,
        fontweight="bold"
    )

    fig.text(
        0.5,
        0.92,
        "Estimated share of population purchasing books in 2020",
        ha="center"
    )

    ax.set_xlabel("Percentage")

    ax.legend()

    ax.grid(axis="x", linestyle="--", alpha=0.5)

    st.pyplot(fig)
    
    st.write("""
The chart compares the percentage of the population purchasing e-books and printed books across several countries in 2020. In all observed countries, printed books account for a higher share than e-books. Germany records the highest proportion of printed book purchases at 58%, followed by France and Spain, both exceeding 49%. In contrast, e-book adoption remains lower, with the United States showing the highest percentage at 22.7%, while countries such as India and France report notably lower figures.

The data indicates a consistent preference for printed books across different markets, despite the availability of digital alternatives. Although e-book usage is present in all countries, its share remains significantly below that of printed books. The variation among countries suggests differences in digital adoption levels and reading habits.

To sum up, the results show that printed books continue to maintain a stronger position in the market, while e-books represent a growing but still smaller segment of total reading consumption.
""")
    
if page == "Plot 6: Top 10 Best-selling Genres":

    st.title("Top 10 Best-selling Genres")

    genres = [
        "Fantasy",
        "Romance",
        "Sci-Fi",
        "Mystery",
        "Thriller",
        "History",
        "Biography",
        "Horror",
        "Comedy",
        "Drama"
    ]

    sales = [15, 14, 12, 10, 9, 8, 7, 6, 5, 4]

    colors = [
        "#FFD6A5",
        "#FFCAD4",
        "#F4ACB7",
        "#FFE5B4",
        "#EFC3CA",
        "#F9DCC4",
        "#FFDAB9",
        "#FBC4AB",
        "#FAE1DD",
        "#D8E2DC"
    ]

    explode = [0.05] * len(genres)

    fig, ax = plt.subplots(figsize=(10, 10))

    wedges, texts, autotexts = ax.pie(
        sales,
        labels=genres,
        colors=colors,
        autopct='%1.1f%%',
        startangle=140,
        explode=explode,
        shadow=True,
        wedgeprops={
            'edgecolor': 'white',
            'linewidth': 2
        },
        textprops={
            'fontsize': 10,
            'color': '#5C4033'
        }
    )

    centre_circle = plt.Circle(
        (0, 0),
        0.55,
        fc='#FFF9F5'
    )

    fig.gca().add_artist(centre_circle)

    ax.set_title(
        "Top 10 Best-selling Genres",
        fontsize=18,
        fontweight='bold',
        color="#6D4C41"
    )

    fig.patch.set_facecolor("#FFF9F5")

    ax.set_facecolor("#FFF9F5")

    st.pyplot(fig)
    
    st.write("""
As transparent from the 3D pie chart, Fiction dominates the book market in terms of book sales, and accounts for 29% of the total sales among the ten best-selling total book sales. Notably, there is a considerable gap between the first and second ranked genres. The proportion of Children’s Fiction is 9% lower than that of Fiction. It is followed closely by Crime, Thrillers & Adventure with merely 1% lower, standing at 19%. In contrast, Young Adult Fiction is only half of the Children’s Fiction at 10%.

Fitness & Diet genre accounts for the least proportion with 2% while Autobiography General and Autobiography: The Art are only 1% more than that of the least-purchased genre. Picture, Food & Drink General and Romance & Sagas comprise 4%, 5% and 6% respectively.

The evaluation shows that Fiction, Children’s Fiction, and Crime, Thrillers & Adventure are the most popular among the top ten most-purchased. Hence, the publisher should invest and focus more on these genres to align with customer preferences and increase profit.
""")
    
if page == "Plot 7: Distribution of Weekly Reading Time by Book Genre":

    st.title("Distribution of Weekly Reading Time by Book Genre")

    genres = [
        "Fantasy",
        "Romance",
        "Sci-Fi",
        "Mystery",
        "Thriller",
        "History",
        "Biography",
        "Horror",
        "Comedy",
        "Drama"
    ]

    reading_hours = [
        8.5,
        7.2,
        6.8,
        5.9,
        5.4,
        4.8,
        4.2,
        3.9,
        3.5,
        3.1
    ]

    colors = [
        "#CDB4DB",
        "#FFC8DD",
        "#BDE0FE",
        "#A2D2FF",
        "#FFD6A5",
        "#CAFFBF",
        "#FDFFB6",
        "#FFADAD",
        "#D8E2DC",
        "#B5EAD7"
    ]

    fig, ax = plt.subplots(figsize=(12, 6))

    bars = ax.bar(
        genres,
        reading_hours,
        color=colors,
        edgecolor='white',
        linewidth=1.5
    )

    for bar in bars:

        height = bar.get_height()

        ax.text(
            bar.get_x() + bar.get_width()/2,
            height + 0.1,
            f"{height} hrs",
            ha='center',
            fontsize=10,
            fontweight='bold',
            color="#555555"
        )

    ax.set_title(
        "Distribution of Weekly Reading Time by Book Genre",
        fontsize=16,
        fontweight='bold',
        color="#444444"
    )

    ax.set_xlabel(
        "Book Genre",
        fontsize=12,
        color="#555555"
    )

    ax.set_ylabel(
        "Weekly Reading Time (Hours)",
        fontsize=12,
        color="#555555"
    )

    plt.xticks(
        rotation=20
    )

    ax.grid(
        axis='y',
        linestyle='--',
        alpha=0.2
    )

    ax.set_facecolor("#FFF9E9")

    fig.patch.set_facecolor("#FFF9E9")

    st.pyplot(fig)
    
    st.write("""
In order to determine if lengthier books are more well valued, the hexbin graphic above looks at the relationship between a book's length and its average reader rating.

The bright yellow cluster, which is centered between 250 and 400 pages, is the most noticeable characteristic. Average ratings are closely packed around the 3.8 to 4.0 line. This shows that the great majority of published publications continuously receive strong, positive evaluations and fall inside this typical page count. The density progressively drops for mid-to-long-range books (between 500 and 1,000 pages), while the average ratings stay steady, mostly remaining strong at 3.5 and 4.5.

The data points become more dispersed yet have a lower vertical spread when we examine extraordinarily large books that are longer than 1,250 pages and up to 2,000 pages. Notably, the majority of these epic volumes maintain a high average rating of between 4.0 and 4.5, with very few receiving low ratings (below 3.0). This implies that readers who devote time to lengthy books are frequently devoted fans who find the whole depth to be very satisfying.

On the other hand, there is a noticeable line of outliers with a score of precisely 0.0 at the lower end of the page spectrum (less than 500 pages), which exhibits the most volatility. This shows that shorter books are more likely to receive extremely poor ratings or unrated entries, and they also experience a far larger variation in reader satisfaction.

Overall, the figure shows that while standard-length books drive the absolute volume in the dataset, expanded page counts enjoy a relatively consistent, premium response, even if there isn't a clear linear trend indicating that longer books are intrinsically better.
""")
    
if page == "Plot 8: Top 10 Most Rated Books":

    st.title("Top 10 Most Rated Books")

    books = pd.DataFrame({

        'title': [
            'Twilight',
            'The Hobbit',
            'Animal Farm',
            'Harry Potter',
            'Angels & Demons',
            'The Ring',
            'The Catcher',
            '1984',
            'Dune',
            'Sherlock Holmes'
        ],

        'ratings_count': [
            4500000,
            2500000,
            2100000,
            2300000,
            2400000,
            2150000,
            2400000,
            2000000,
            1900000,
            1800000
        ]
    })

    books = books.sort_values('ratings_count')

    colors = [
        "#FFD6A5",
        "#FFCAD4",
        "#F4ACB7",
        "#FFE5B4",
        "#EFC3CA",
        "#F9DCC4",
        "#FFDAB9",
        "#FBC4AB",
        "#FAE1DD",
        "#D8E2DC"
    ]

    fig, ax = plt.subplots(figsize=(12, 7))

    for i in range(len(books)):

        ax.hlines(
            y=books['title'].iloc[i],
            xmin=0,
            xmax=books['ratings_count'].iloc[i],
            color=colors[i],
            linewidth=6,
            alpha=0.9
        )

    ax.scatter(
        books['ratings_count'],
        books['title'],
        s=250,
        color=colors,
        edgecolors='white',
        linewidth=2,
        zorder=3
    )

    for i in range(len(books)):

        ax.text(
            books['ratings_count'].iloc[i] + 50000,
            books['title'].iloc[i],
            f"{books['ratings_count'].iloc[i] / 1000000:.1f}M",
            va='center',
            fontsize=10,
            color="#6D4C41",
            fontweight='bold'
        )

    ax.set_title(
        "Top 10 Most Rated Books",
        fontsize=18,
        fontweight='bold',
        color="#6D4C41"
    )

    ax.set_xlabel(
        "Ratings Count",
        fontsize=12,
        color="#6D4C41"
    )

    ax.set_ylabel(
        "Books",
        fontsize=12,
        color="#6D4C41"
    )

    ax.set_facecolor("#FFF9F5")

    fig.patch.set_facecolor("#FFF9F5")

    ax.grid(
        axis='x',
        linestyle='--',
        alpha=0.2
    )

    st.pyplot(fig)
    
    st.write("""
The lollipop chart presents the top 10 most rated books, along with their total number of ratings and average rating levels.

Overall, certain books stand out as significantly more popular than others, with a notably higher number of ratings. However, high popularity does not always correspond to the highest average rating, indicating differences between widespread appeal and user satisfaction.

In detail, Twilight (Twilight #1) has the highest number of ratings, making it the most widely reviewed book in the dataset. Several titles from the Harry Potter series also appear frequently, demonstrating strong and consistent reader engagement. Additionally, classic and well-known titles such as The Hobbit or There and Back Again and The Catcher in the Rye maintain high levels of popularity. In terms of average rating, variations can be observed across books, as indicated by differences in color intensity. Some books with slightly lower total ratings achieve higher average ratings, suggesting that niche or less widely read books may receive more favorable evaluations.

In conclusion, the chart highlights that while certain books dominate in terms of popularity, reader ratings vary across titles. This suggests that popularity and perceived quality are related but not always directly proportional, reflecting diverse reader preferences and evaluation standards.
""")
    
if page == "Plot 9: Top 10 Authors by Number of Books":

    st.title("Top 10 Authors by Number of Books")

    data = {
        'authors': [
            'Stephen King',
            'Agatha Christie',
            'James Patterson',
            'Sandra Brown',
            'Piers Anthony',
            'Dick Francis',
            'Rumiko Takahashi',
            'P.G. Wodehouse',
            'Mercedes Lackey',
            'Orson Scott Card'
        ],

        'n': [40, 33, 23, 29, 30, 28, 39, 40, 29, 35]
    }

    df = pd.DataFrame(data)

    colors = [
        "#A2D2FF",
        "#BDE0FE",
        "#CDB4DB",
        "#B5EAD7",
        "#A0E7E5",
        "#D0F4DE",
        "#C7CEEA",
        "#B5D8EB",
        "#AEC6CF",
        "#CDE7F0"
    ]

    fig, ax = plt.subplots(figsize=(12, 7))

    bars = ax.barh(
        df['authors'],
        df['n'],
        color=colors,
        edgecolor='white',
        linewidth=2
    )

    for bar in bars:

        width = bar.get_width()

        ax.text(
            width + 0.5,
            bar.get_y() + bar.get_height()/2,
            f"{int(width)}",
            va='center',
            fontsize=10,
            fontweight='bold',
            color="#4A6572"
        )

    ax.set_title(
        "Top 10 Authors by Number of Books",
        fontsize=18,
        fontweight='bold',
        color="#4A6572"
    )

    ax.set_xlabel(
        "Number of Books",
        fontsize=18,
        color="#4A6572"
    )

    ax.set_ylabel(
        "Authors",
        fontsize=18,
        color="#4A6572"
    )

    ax.set_facecolor("#F6FBFF")

    fig.patch.set_facecolor("#F6FBFF")

    ax.grid(
        axis='x',
        linestyle='--',
        alpha=0.2
    )

    st.pyplot(fig)
    
    st.write("""
The horizontal bar chart above compares the number of works produced by the top 10 authors, showing the number of books attributed to each writer. The data includes a wide variety of genres, from horror and detective to comics and comedy.

In the leading group, Stephen King and P.G. Wodehouse are the two most productive authors, each having reached the 40-book mark. Following closely behind them is Rumiko Takahashi, who has published 39 books, just one book short of the leader. For mid-level authors, Orson Scott Card and Agatha Christie are highly productive, with 35 and 33 books, respectively.

The lower half of the ranking includes authors such as Piers Anthony (30), followed by Sandra Brown and Mercedes Lackey with 29 books each. Dick Francis is close behind with 28 books. The entry "James Patterson" in this particular collection has the fewest volumes, showing a significantly smaller number than the leaders, ending at 23 books.

Overall, there is a clear disparity in output recorded within this collection. While the top three authors exhibit exceptionally high and similar levels of productivity (39-40 books), there is a gradual decline towards the end of the list, with James Patterson representing the minimum threshold of this top 10 group of authors.
""")
    
if page == "Plot 10: Distribution of Author Ratings: Fiction vs. Non-fiction":

    st.title("Distribution of Author Ratings: Fiction vs. Non-fiction")

    ratings = ['Novice', 'Intermediate', 'Famous', 'Excellent']

    fiction = [25, 510, 40, 260]

    nonfiction = [10, 90, 15, 75]

    fig, ax = plt.subplots(figsize=(12, 7))

    fiction_color = "#95D5B2"
    nonfiction_color = "#D8F3DC"

    ax.barh(
        ratings,
        fiction,
        color=fiction_color,
        edgecolor='white',
        linewidth=2,
        label='Fiction'
    )

    ax.barh(
        ratings,
        [-x for x in nonfiction],
        color=nonfiction_color,
        edgecolor='white',
        linewidth=2,
        label='Non-fiction'
    )

    ax.axvline(
        0,
        color='#52796F',
        linewidth=2
    )

    for i in range(len(ratings)):

        ax.text(
            fiction[i] + 5,
            ratings[i],
            str(fiction[i]),
            va='center',
            fontsize=18,
            fontweight='bold',
            color="#2D6A4F"
        )

        ax.text(
            -nonfiction[i] - 15,
            ratings[i],
            str(nonfiction[i]),
            va='center',
            fontsize=18,
            fontweight='bold',
            color="#2D6A4F"
        )

    ax.set_title(
        "Distribution of Author Ratings",
        fontsize=18,
        fontweight='bold',
        color="#2D6A4F"
    )

    ax.set_xlabel(
        "Number of Authors",
        fontsize=18,
        color="#2D6A4F"
    )

    ax.set_ylabel(
        "Rating Category",
        fontsize=18,
        color="#2D6A4F"
    )

    ax.set_facecolor("#F1FAEE")

    fig.patch.set_facecolor("#F1FAEE")

    ax.grid(
        axis='x',
        linestyle='--',
        alpha=0.2
    )

    ax.legend()

    st.pyplot(fig)
    
    st.write("""
The analysis of book counts reveals a non-linear relationship between an author's rating and their total output. While one might expect a steady increase in productivity as authors gain experience, the data shows a massive surge, specifically at the Intermediate level. This suggests that the "Intermediate" stage is the most prolific period for authors, possibly because it balances established skill with high creative energy.

A striking observation is the dominance of Genre Fiction across almost all ratings. For Intermediate and Excellent authors, fiction titles outnumber nonfiction by a wide margin reaching a peak of over 500 books for Intermediate fiction. This indicates that the fiction market is likely the primary engine of growth and volume in the industry.

In contrast, the Novice and Famous groups show the lowest output. For Novices, this likely represents the "barrier to entry" in the publishing world. For Famous authors, the lower count compared to the Intermediate group suggests a shift from quantity to quality, where established icons may focus on a few high-impact releases rather than high-volume production. Ultimately, the chart highlights that while fiction drives the numbers, the Nonfiction sector remains a steady, albeit smaller, specialized niche across all professional tiers.
""") 
    
    
# CUSTOM THEME

st.markdown("""
<style>

.main {
    background: linear-gradient(to right, #fdfbfb, #ebedee);
}

.stMarkdown,
.stText,
p,
div[data-testid="stMarkdownContainer"] p {
    font-size: 18px !important;
    line-height: 1.8;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(to bottom, #6C63FF, #4EA8DE);
    color: white;
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

h1, h2, h3 {
    color: #4B3F72;
    font-family: 'Trebuchet MS', sans-serif;
}

.stPlotlyChart, .stPyplotGlobalUse {
    background-color: white;
    padding: 15px;
    border-radius: 18px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.08);
}

div[data-baseweb="radio"] > div {
    background-color: rgba(255,255,255,0.12);
    padding: 10px;
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)

sns.set_style("whitegrid")

plt.rcParams['figure.facecolor'] = '#F8F9FF'
plt.rcParams['axes.facecolor'] = '#FFFFFF'
plt.rcParams['axes.edgecolor'] = '#DDDDDD'
plt.rcParams['axes.labelcolor'] = '#444444'
plt.rcParams['xtick.color'] = '#555555'
plt.rcParams['ytick.color'] = '#555555'
plt.rcParams['font.size'] = 11