def fetch_user_info():
    # Collect student's complete information
    info = {
        "name": "Ayush Yadav",
        "school": "JEC Jabalpur",
        "major": "Information Technology",
        "year": "Final Year",
        "skills": ["Python", "Devops", "Native Android Development"]
    }

    resume_dict = {
        'personal_info': {
            'Name': 'Ayush Yadav',
            'Email id': 'ayushyadavcodes@gmail.com',
            'education': [
                {
                    'institution': 'Jabalpur Engineering College',
                    'years': '2020-2024',
                    'degree': 'Bachelor of Technology in Information Technology',
                    'cgpa': '7.84',
                }
            ]
        },
        'experience': [
            {
                'title': 'Product Engineering Intern',
                'company': 'Dashtoon',
                'time_period': 'May 2023 – Present',
                'location': 'Bengaluru',
                'details': [
                    'Working on ML Infra, Devops, Python Backend and Automation',
                    'Reduced Training cost by converting GPU based service to on demand job deployer, FastAPI app, deployed on Truefoundry',
                    'Implemented a comprehensive logging pipeline with Fluent-bit, OpenTelemetry Collector, Loki, and Grafana for efficient troubleshooting in Kubernetes production settings'
                ],
                'technologies': ['Python', 'Docker', 'Kubernetes', 'Truefoundry', 'Github Actions', 'AWS', 'Azure', 'Slack bots', 'FastAPI backend', 'PostgreSQL', 'Unreal Engine automation', 'cron scripts']
            },
            {
                'title': 'Android Developer Intern',
                'company': 'Online Thela',
                'time_period': 'April 2022 – May 2022',
                'details': [
                    'Developed OnlineThela App - an Android App made with kotlin to work as MVP for Startup.',
                    'Implemented Single Activity Architecture using Jetpack Navigation Component.',
                    'Converted Figma Designs to Optimised App UI to support Multiple Phone Screens.',
                    'Collaborated with multiple Interns using Git. Created and Merged Multiple PRs.'
                ],
                'skills': ['Recycler View', 'Fragments', 'Shared Preferences', 'JSON Objects', 'API Requests Using Volley (GET, PUT, POST, DELETE)', 'Glide Library']
            }
        ],
        'projects': [
            {
                'name': 'BeFrend',
                'time_period': 'June 2022 - Jan 2023',
                'details': [
                    'A platform to find your college peers based on interests and skills.',
                    'Features: Google and Email Login, Customise Profile, Send, Cancel and Accept Request, User Chat'
                ],
                'technologies': ['Jetpack Navigation Component', 'Fragments', 'Firebase Auth', 'Cloud Firestore', 'Firebase Storage', 'Image Compression', 'BlurView and Glide Library', 'ViewBinding', 'Caching data with Shared ViewModel', 'Swipeable Cards UI']
            },
            {
                'name': 'NoteZen - Notes App',
                'time_period': 'February 2022',
                'details': [
                    'Created a Notes App with Firebase db and Google Authentication',
                    'CRUD Functionality using Cloud Firestore',
                    'Clean UI - Custom Toolbar, Swipe to Delete using Card View'
                ]
            }
        ],
        'achievements': [
            {
                'details': 'Contributed to the WordPress-Android by fixing issue 17676 and successfully merging PR 17934',
                'time': 'Feb 2023'
            },
            {
                'details': 'Flipkart Grid 4.0 Semifinalist, My Team was in Top 50 teams from 13,000+ Participants.',
                'time': 'July 2022'
            }
        ],
        'technical_skills': {
            'languages_and_dbs': ['C++', 'Kotlin', 'Python', 'Firebase Cloud Firestore', 'Room DB - SQLite', 'PostgreSQL'],
            'frameworks_and_technologies': ['Android SDK', 'Docker', 'Kubernetes', 'Truefoundry', 'FastAPI backend', 'Git & GitHub', 'Cloud: AWS', 'Azure'],
            'android_dev_skills': ['Volley', 'Glide', 'Recycler View', 'Firebase', 'REST API', 'Shared Preferences', 'Jetpack Navigation Component', 'Kotlin Coroutines', 'ViewBinding']
        }
    }

    return resume_dict
