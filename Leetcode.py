from model import ProcessData
import selenium_dloader
import heapq


input_url = "https://leetcode.com/problems/two-sum/"
depth = 2
visited = set()
crawler_log = open("Logs/crawler_log.txt","w")


def level_crawler(input_url , level):
    queue = []
    print(input_url)
    links_dict = selenium_dloader.dynamic_loading(input_url)
    crawler_log.write(f"---------------Level $$${level}$$$----------------\n")
    for anchor in links_dict.keys():
        val = None
        if links_dict[anchor] == "Easy":
            val = 1
        elif links_dict[anchor] == "Medium":
            val = 2
        else:
            val = 3        
        heapq.heappush(queue, (val , anchor))

    # print(queue)
    for url in queue:
        print("hii")   
        crawler_log.write(str(url[1])+") "+str(links_dict[url[1]])+"\n") 

    crawler_log.write("Finish these first then move Forward\n")    
    return queue    
                

if(depth == 0):
    print("Intern - {}".format(input_url))

elif(depth == 1):
    level_crawler(input_url)

else:
    queue = []
    queue.append(input_url)
    for j in range(depth):
        for count in range(len(queue)):
            url = queue.pop(0)
            urls = level_crawler(url , j+1)
            
            for i in urls:
                if i in visited:
                    continue
                queue.append(i[1])
                visited.add(i[1])
