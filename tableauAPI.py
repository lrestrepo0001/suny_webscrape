import tableauserverclient as TSC

tableau_auth = TSC.TableauAuth('lr2956@tc.columbia.edu', 'xEIi910bbf8e', 'https://10ax.online.tableau.com/#/site/mylrcomdev628667/home')
server = TSC.Server('https://tableauserver.suny.edu/t/IRPublic/views/PublicDashboard-ADAChanges/Dashboard?%3Aembed=y&%3AshowVizHome=no&%3Ahost_url=https%3A%2F%2Ftableauserver.suny.edu%2F&%3Aembed_code_version=3&%3Atabs=yes&%3Atoolbar=yes&%3AshowAppBanner=false&%3Adisplay_spinner=no&%3AloadOrderID=0')

with server.auth.sign_in(tableau_auth):
    all_datasources, pagination_item = server.datasources.get()
    print("\nThere are {} datasources on site: ".format(pagination_item.total_available))
    print([datasource.name for datasource in all_datasources])

