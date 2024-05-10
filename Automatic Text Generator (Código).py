"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

genai.configure(api_key="AIzaSyDPbxDvSPoa4p0XKq1SpMeuXCppD3xW9M8")

# Set up the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 0,
  "max_output_tokens": 8192,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

prompt_parts = [
  "Tipo de Texto Texto informativo e com agradecimentos",
  "Contexto Semear da GRE Metrosul",
  "output: Ontem foi um dia de inspiração, aprendizado e conexão no SEMEAR 2024.1 da GRE Metropolitana Sul! Agradecemos a todos os alunos, professores e colaboradores que tornaram esse evento possível. Juntos, protagonizamos momentos inesquecíveis de crescimento e compartilhamos experiências enriquecedoras. Até o próximo SEMEAR! 🤩📚",
  "Tipo de Texto Faça um texto informativo e com breve convite",
  "Contexto Inicio do Terço nas Praças da Comunidade São João Batista",
  "output: Ontem, demos início ao terço nas praças da Comunidade São João Batista, o terço com a mãe peregrina acontecerá todas as quartas pelas praças da nossa comunidade. Siga atento nas nossas redes e nos avisos da comunidade para acompanhar-nos nessa missão evangelizadora!",
  "Tipo de Texto Texto informativo (mais detalhado), com agradecimentos e convites para o serviço na igreja",
  "Contexto Crisma da Paróquia Nossa Senhora do Rosário",
  "output: Neste sábado, dia 04 de maio, foi realizado na Imperial Matriz do Rosário, a celebração do Sacramento da Crisma. Na ocasião, 70 jovens de nossa paróquia e estavam se preparando receberam o Sacramento. O presidente da celebração foi o Monsenhor Josivaldo Bezerra, vigário geral de nossa arquidiocese. Rezemos por esses jovens para que perseverem na igreja e sejam instrumentos de Deus nas pastorais, grupos e movimentos de nossa Paróquia e levem Cristo por onde passarem. Que o Espírito Santo seja o guia e que eles se permitam ser usados por Deus.Que a Virgem Mãe do Rosário, nossa Excelsa padroeira os abençoe, guarde e proteja. #crisma #sacramento #igrejacatolica #paroquiadavarzea",
  "Tipo de Texto Convite detalhado para os estudantes com link para inscrição",
  "Contexto Programa Ganhe o Mundo de Pernambuco",
  "output: 📣🌟 Atenção estudantes da Metro Sul! 🌟📣As inscrições para os incríveis aulões preparatórios do Ganhe o Mundo estão oficialmente abertas! 📚✨Se você tem entre 14 e 16 anos e está cursando o 1º ou 2º ano, essa é a sua chance de se preparar para brilhar no idioma inglês ou espanhol. 🌍💡Confira as datas dos aulões e os polos mais próximos da sua casa:🗓️ Datas:18/05 - 25/05 - 01/06 - 08/06 - 15/06 - 29/06 Não perca essa oportunidade única de aprimorar seus conhecimentos e se preparar para o futuro! 🚀✨Para se inscrever, clique no link em nossa bio. 📝👆Ou acesse: https://docs.google.com/forms/d/1LQAONsDgZ-Ijj0lkmHtfJ_PWmfVJy0JQZcORxhiSWac/edit#gremetrosul #educação #pernambuco #ganheomundo",
  "Tipo de Texto Texto Informativo",
  "Contexto Reunião de alinhamento com os coordenadores Gerais da Rede de Ensino",
  "output: Um marco no caminho da excelência educacional! Na última reunião de alinhamento da Coordenação Técnica de Gestão, onde tivemos a honra de contar com a presença e colaboração de 10 coordenadores gerais da Rede, fortalecemos nosso compromisso com a excelência educacional. Juntos, estamos pavimentando o caminho para uma gestão mais integrada e eficiente, com foco no desenvolvimento contínuo de nossos educadores e no sucesso de nossos estudantes. 📚💡...#gremetrosul #educação #pernambuco",
  "Tipo de Texto Texto informativo e de agradecimento",
  "Contexto Dia nacional da matemática no Erem Poeta Mauro Mota",
  "output: Hoje comemoramos o Dia Nacional da Matemática e os alunos da EREM Poeta Mauro Mota têm um recado importante sobre esta data! Nas nossas escolas, estão acontecendo atividades direcionadas a esse dia. 📚Aproveitamos, também, para parabenizar os professores da área que têm como missão a divulgação dessa ciência. 👩‍🏫👨‍🏫Que possamos fazer dos estudos matemáticos uma vivência para o nosso cotidiano! Vivam os números e suas diversas possibilidades! 🔢🤩",
  "Tipo de Texto Texto jornalistico",
  "Contexto Ministro da Educação Visita Porto Digital",
  "output: Nesta quinta-feira (09), Camilo Santana, Ministro da Educação, esteve no Porto Digital para conhecer os programas de formação de capital humano na área de tecnologia do nosso ecossistema.No encontro, ele foi recepcionado por Pierre Lucena, presidente do Porto Digital e pelo prefeito João Campos que pontuaram como um dos programas de formação, o Embarque Digital - iniciativa pioneira do ecossistema que tem potencial ampliação a nível nacional por ser um modelo de sucesso em educação e inovação tecnológica no Brasil.Saiba mais no Jornal Digital clicando no link em nossa bio. 👩🏻‍💻#tecnologiaeducação #tecnologiarecife #educaçãorecife #portodigital #embarquedigital",
  "Tipo de Texto Texto informativo",
  "Contexto Accenture oferece vagas de emprego para o nordeste e sudeste",
  "output: São mais de 100 oportunidades de emprego abertas distribuídas em 10 funções - todas na área da tecnologia. Há vagas para Paraíba, Ceará, Pernambuco, São Paulo, Rio de Janeiro e Minas Gerais.Confira as oportunidades no Jornal Digital pelo link em nossa bio.",
  "Tipo de Texto Texto informativo e convidativo",
  "Contexto Oficina sobre o uso da IA no marketing",
  "output: Essa Jump Sessions traz como temática \"O Uso de IA no Marketing Digital\" com Socorro Macedo, sócia fundadora da Le Fil Company e Raquel Laureano, da área de Relacionamento Educacional da CESAR School.Durante o painel, as especialistas irão trazer suas experiências utilizando IA para ações de Marketing Digital, com dicas e um momento para tirar dúvidas do público. Será um bate-papo bem dinâmico, mediado pelo nosso coordenador de empreendedorismo, Daniel Lima.Realize sua inscrição agora mesmo pelo link em nossa bio e vem participar com a gente no dia 08 de maio, às 19h, no Porto Digital (Auditório Pontes, 8o andar). #portodigital #portodigitalrecife #inovação #tecnologiarecife #portodigitalrecife#marketingdigital",
  "Tipo de Texto Texto informativo/convidativo para o evento",
  "Contexto Evento Mind the beerz do Porto digital (evento para networking)",
  "output: É happy hour que vocês querem? 😄O Mind The Beerz voltou e agora, a cada dois meses, teremos um encontro marcado aqui no Porto Digital para se conectar e conhecer as startups de nossa Comunidade.O evento contará com microfone aberto, para vocês se apresentarem em pitches de até um minuto.Já coloca na agenda: amanhã (30/04), a partir das 17h no Auditório Pontes (Cais do Apolo, 222, sede do Porto Digital). 😄Faça sua inscrição no link em nossa bio.#inovação #tecnologiarecife #startups #recife #portodigital",
  "Tipo de Texto Texto jornalistico",
  "Contexto Desafio para a presidencia brasileira, as enchentes que assolam o povo da região sul",
  "output: \"Teste crucial para a liderança de Lula\" 📰🌎⁠⁠Nos últimos dias, vários veículos da imprensa internacional destacaram as enchentes no sul do Brasil.⁠⁠Uma análise da agência Bloomberg diz que esse será um dos momentos definidores da Presidência de Lula:⁠⁠\"Os assessores [de Lula] dizem que ele está perfeitamente consciente de que este pode ser o seu 'momento Katrina', uma referência ao furacão de 2005 que pegou o presidente dos EUA, George W. Bush, desprevenido e entrou no vocabulário global como sinônimo de fracasso de liderança em uma crise\", afirma o texto da Bloomberg, assinado por Travis Waldron.⁠⁠A agência disse que Lula reagiu às enchentes com atendimento às necessidades básicas dos afetados, viajando à região e assinando um decreto que retira os gastos emergenciais das regras fiscais.⁠⁠\"Com mais chuva e temperaturas em queda previstas durante a semana, os desafios só vão aumentar\", diz o texto da Bloomberg.⁠⁠\"Isso pode dar a Lula a oportunidade de recuperar uma presidência assolada nos últimos meses por rivalidades internas, brigas com o Congresso, escrutínio do mercado sobre os seus planos de gastos e popularidade em declínio.\"⁠⁠O jornal britânico Financial Times destacou o prejuízo financeiro do Estado — estimado na ordem de R$ 5 bilhões.⁠⁠O Washington Post, principal jornal da capital americana, também noticiou as enchentes.⁠⁠\"Mesmo em um país cada vez mais habituado a desastres naturais provocados pelas alterações climáticas, as inundações que engoliram o Rio Grande do Sul — um dos Estados mais desenvolvidos e prósperos do Brasil — abalaram gravemente esta nação de 215 milhões de habitantes. Com mais da metade das cidades do Estado enfrentando enchentes [...], o Rio Grande do Sul não foi apenas afetado. Foi arrasado.\"⁠⁠Leia mais sobre a repercussão internacional das enchentes no Sul em nossa reportagem. O link está na bio: @BBCBrasil⁠⁠#BBCBrasil #riograndedosul #enchentes #inundacoes #clima #imprensa #meioambiente",
  "Tipo de Texto ",
  "Contexto ",
  "output: ",
]

response = model.generate_content(prompt_parts)
print(response.text)
