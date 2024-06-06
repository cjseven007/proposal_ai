from event_details import EventDetails
system_message = '''
    You are an AI assistant specializing in writing event proposals for university events.
    You are currently working in Universiti Teknologi PETRONAS.
    Your primary objective is to prepare a proposal template tailored to specific events.
    In each proposal, you MUST include introduction, 3 objectives, 3 critical issues, and conclusion.
'''


def list_three(text, title, description):
    three_ans_template = f'List 3 {text} with short explanation of one sentence each about {title} which is {description}.'


def get_prompt(event):
    objectives_template = list_three(
        "objectives", event.title, event.description)
    critical_issues_template = list_three(
        "negative consequences what will happen if the event is not organized", event.title, event.description)

    prompt = f'''
        For introduction, you can start with '{event.title} is {event.description} which will be organized by {event.club} on {event.date} from {event.start_time} to {event.end_time} at {event.venue}.'
        1. Write the introduction about the event {event.title} which is {event.description} in less than 150 words.
        2. List 3 Objectives
        3. In the critical issues section, list 3 consequences if the event is not carried out.
        4. Write a conclusion about the event {event.title} which is {event.description} in less than 150 words.
'''
    return prompt
