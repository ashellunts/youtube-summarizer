from src import app
import pytest


@pytest.fixture
def test_client():
    with app.get_server().test_client() as test_client:
        yield test_client


EXPECTED_RESPONSE = '<div>\n\n<p>Brooke Shields discusses her experiences with objectification and the sexualization of young girls in the entertainment industry. She speaks about the pressure to be desirable to straight men and gatekeeping as a way to control young girls. Shields found her confidence and agency through her own experiences and encourages others to do the same. The cultural environment can be toxic and many people have a similar narrative to Shields&#39;. She questions what could have happened if she wasn&#39;t born with beauty.</p>\n\n</div>'


@pytest.mark.vcr()
def test_make_summary_api_1_copy(test_client):
    query_string = {'video_url': 'https://www.youtube.com/watch?v=x7KedT6uvus'}
    response = test_client.post('/api2', query_string=query_string)
    assert response.status_code == 200
    assert EXPECTED_RESPONSE == response.text


EXPECTED_RESPONSE_2 = '<div>\n\n<p>The video is about using Vim to solve a bug in the Chad stack while developing a web application. The bug involves a missing directory, which the user navigates using various Vim plugins such as Telescope and Harpoon. They demonstrate how to find the bug and fix it by creating the necessary directory and implementing some code changes. The video also includes tips for improving navigation in Vim.</p>\n\n<p>The video covers how to use Vim to make changes to a project&#39;s code and how to work with Git. The speaker demonstrates using various commands to create and resolve a merge conflict within Git. He also shows how to use a Vim plugin called Context Tree Sitter to display the current file&#39;s changes and the use of keyboard shortcuts to speed up workflow efficiency. The speaker encourages viewers to like and subscribe for more content and to express interest in a workflow tutorial for Tmux, I3, and Vim.</p>\n\n</div>'


@pytest.mark.vcr()
def test_make_summary_api_video_that_needs_2_api_calls(test_client):
    query_string = {'video_url': 'https://www.youtube.com/watch?v=FrMRyXtiJkc'}
    response = test_client.post('/api2', query_string=query_string)
    assert response.status_code == 200
    assert EXPECTED_RESPONSE_2 == response.text


EXPECTED_RESPONSE_3 = '<p><b>TLDR</b></p>\n<p>Google director of engineering Jeffrey Van Gogh interviews Steve McConnell, the author of &#34;Code Complete,&#34; in a discussion about programming languages, readable and maintainable code, and the evolution of full-stack development. The group also offers advice for programmers, including writing code, learning from experience, and engaging in peer review and collaboration. McConnell emphasizes the importance of gaining experience through internships and real-world projects while providing background in his research for &#34;Code Complete.&#34;</p>\n<p><b>Longer version</b></p>\n<div>\n\n<p>Jeffrey van Gogh, a director of engineering at Google, interviews Steve McConnell, the author of &#34;Code Complete,&#34; about the evolution of programming languages and the impact on coding practices. They discuss the importance of readable and maintainable code, the use of comments and external documentation, and the role of tooling in aiding comprehension of large codebases. They also touch upon the changes in full-stack development, as programmers now tend to work with multiple languages across various platforms.</p>\n\n<p>The speaker discusses their role in hiring for their team and how they prioritize skills in compilers over skills in specific programming languages. They also discuss their favorite and least favorite features of Kotlin, as well as the importance of programmers being exposed to real-life programs and open-source projects. They touch on supply chain security concerns with open-source libraries and the potential for errors when reusing code in unintended ways. One of the controversial standpoints in the book is the use of i, j, and k for indexes, which the speaker sees as lazy and a missed documentation opportunity.</p>\n\n<p>In the third part of the video, the speaker argues that using variable names like &#34;i&#34; in code is not ideal for readability and can lead to errors. They discuss their personal coding projects during the pandemic and how they approached them differently. The topic of managers who code is also discussed, with the speaker arguing that while it&#39;s good for managers to remain technical, it&#39;s not necessary for them to write production code and they should focus on developing soft skills. The speaker also mentions the extensive research they did for their book, which includes numerous references to other literature.</p>\n\n<p>In the video, the author talks about how he researched for &#34;Code Complete,&#34; his best-selling book on software construction. He read over 600 articles and books to find information that was not available in other books. He also emphasizes the importance of peer review and collaboration in writing a book. He recommends that new programmers write as much code as possible and learn from experience, as well as read and learn from other people&#39;s code. Some university students find the &#34;before&#34; case studies unrealistic, while professionals in the field relate to them. The author suggests that students do internships to gain real-world experience.</p>\n\n</div>'


@pytest.mark.vcr()
def test_make_summary_api_video_that_needs_tldr(test_client):
    query_string = {'video_url': 'https://www.youtube.com/watch?v=STpbPXW9-pA'}
    response = test_client.post('/api2', query_string=query_string)
    assert response.status_code == 200
    assert EXPECTED_RESPONSE_3 == response.text
