# readXML.py
import pantherine as purr

def main():
    map_dir = "../TAPASCologne-0.32.0"
    print("map dir=%s" % (map_dir))
    
    # Retrieve the rou.xml file
    trips_xml = purr.mrf(map_dir,r'*trips.xml')
    print("trips.xml=%s" % (trips_xml))
    
    # Load the trips into a dictionary type
    trips = purr.readXMLtag(trips_xml,'trip')
    print("First five trips.")
    purr.head(trips,5)
    
    # The data will be read into a dictionary as a string type
    # YOu can acess them like this.
    print('id=%s' % (trips[0]['id']))
    print('depart time=%.2f' % (float(trips[0]['depart'])))
    return

if __name__ == "__main__":
    main()
