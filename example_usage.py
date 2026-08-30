from client import IterativeMultiStepWebResearchSynthesizerClient

def main():
    client = IterativeMultiStepWebResearchSynthesizerClient()
    res = client.execute_deep_research_synthesis('Semiconductor lithography EUV vs High-NA EUV yield rates in 2nm nodes')
    print('Deep Research Synthesizer: ' + res['research_session_id'] + ' (' + str(res['search_iterations_executed']) + ' iterations)')
    print('Sources Scraped: ' + str(res['web_sources_scraped_count']) + ' | Contradictions Resolved: ' + str(res['contradictions_resolved_count']))
    print('Factual Grounding: ' + str(res['factual_grounding_score_pct']) + '%')
    print('Report: ' + res['deep_research_report_url'])

if __name__ == '__main__':
    main()
