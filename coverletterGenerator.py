from datetime import datetime


name='Divesh Chudasama'
address = '66 Watershed Gate'
phonenum = '647-970-1494'

today = datetime.today().strftime('%Y-%m-%d')
jobname = input("What is the position: ")
company = input("What company: ")

letter = f"""
    {address}
    {phonenum}
    {today}

    Dear Hiring Manager,

    I am writing to express my interest in the {jobname} position at {company}. As a Fullstack Developer at Norconsult, I've played a key role in enhancing our business intelligence app, implementing diverse visualizations using CraftJS, ChartJS, Leaflet, and React libraries. I improved data accessibility by designing a system to access various sources and storing data in PostgreSQL. Strengthening data analysis capabilities, I utilized CubeJS for querying, measures, and dimensions. Additionally, I developed a robust REST API using Node.js, Express, middleware, and Winston to enhance application functionality and reliability. I also contributed to AI and machine learning advancements through research and prototyping.

    My recent project, the Heads-Up Display Smart Helmet, received the "Best Safety Analysis" award, showcasing my innovation. I developed and tested it using Raspberry Pi 4 and Pi Camera for real-time video stream processing. Implementing object detection using TensorFlow lite models, I optimized performance with a transition from Python to C++. Demonstrating expertise in embedded systems design, I addressed task management through multiprocessing and multithreading.

    I am eager to contribute my technical skills, creativity, and dedication to {company}'s success. I believe my experience aligns well with your team's needs, and I look forward to discussing how I can make meaningful contributions.

    Thank you for considering my application. I look forward to the possibility of an interview.

    Sincerely,

    {name}
"""

print(letter)