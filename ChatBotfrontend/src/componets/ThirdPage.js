import React, {useState} from "react";
import { View, Text, TouchableOpacity, Image, StyleSheet, Modal, Button } from "react-native";
import {data} from './Data';
import TalkToMurimiButton from './MurimiButton';
import HomeIcons from "./HomeIcons";

const homeIcon = `../../assets/home.svg`;
const marketIcon = `../../assets/market.svg`;
const settingsIcon = `../../assets/settings.svg`;


const ThirdPage = () => {

  const [showModal, setShowModal] = useState(false);

  const handleImageClick = (text) => {
    setShowModal( !showModal);
    ;
  };


  return (
    <View>
    <Text style={styles.mainHeading}>Hi, How may l be of assistance today?</Text>
    <View style={styles.container}>
      {data.map((item, index) => (
        <TouchableOpacity
          key={index}
          style={styles.imageContainer}
          onPress={() => handleImageClick(item.text)}
        >
          <Image source={item.image} style={{height:item.height, ...styles.image}} />
          <View 
            style={{height:item.innerHeight, ...styles.innerContainer}}
          >
              <Image source={item.icon} style={styles.icon} />
              <Text style={styles.imageText}>{item.text}</Text>
              <Text style={styles.subText} >{item.subText}</Text>
          </View>
          <Modal
              isOpen={index === showModal}
              animationType={'fade'}
              transparent={false}
              onRequestClose={() => setShowModal(false)}
              visible={showModal}
            >
              <View style={styles.modalText}>
                <View>
                  <Image source={item.image} style={styles.flexImage}/>
                  <View style={styles.flexItems}>
                    <Image source={item.icon} style={styles.flexIcon} />
                    <Text style={styles.flexText} >{item.text}</Text>
                  </View>
                  <View style={styles.flexContent}>
                <Text style={styles.flexHeading}>About</Text>
                
                <Text style={styles.flexSubtext}>
             
                Soil preparation is a crucial step in gardening and 
                agriculture that involves getting the soil ready for 
                planting or seeding.  
                {"\n"}
                {"\n"}
                    Here's a summary of soil preparation:
                    {"\n"}
                    1. Clearing the Area:
                    {"\n"}
                    2. Soil Testing
                    {"\n"}
                    3. Soil Aeration
                    {"\n"}
                    4. Organic Matter Addition
                    {"\n"}
                    5. Soil Amendments
                    {"\n"}
                    6. Weed Control
                    {"\n"}
                    7. Leveling and Smoothing
                    {"\n"}
                    8. Irrigation Preparation

                          For more information
                </Text>
                <TalkToMurimiButton/>

                </View>
                </View>
              </View>
              <Button
                style={styles.flexButton}
                title="Back"
                onPress={() => {
                  setShowModal(false);
                }}
              />            
          </Modal>
        </TouchableOpacity>
      ))}
      <TalkToMurimiButton/>
      <HomeIcons/>
      <View style={styles.greenBorder} /> 

    </View>
    </View>

  );
};


const styles = StyleSheet.create({
  container: {
    flex: 1,
    flexDirection: "row",
    flexWrap: "wrap",
    justifyContent: "space-between",
    paddingHorizontal: 22,
    position: 'relative'
  },

  flexItems:{
    flexDirection: "row",
    justifyContent: "center",
    alignItems: "center",
    position:'absolute',
    paddingLeft:50,
    paddingTop:50
  },
  flexContent:{
    marginLeft:10,
    backgroundColor:'white',
    width:'95%',
    paddingTop:10,
    paddingLeft:20,
    paddingRight:20,
    paddingBottom:50,
    bottom:18,
  },
  flexHeading:{
    fontWeight:500,
    fontSize:18,
    color:'black',
  },
  flexSubtext:{
    color:'#545454',
    fontSize:14,
    lineHeight:20
  },
  flexImage:{
    height:180,
    width:'95%',
    borderRadius: 20,
    marginLeft:10

  },

  flexText:{
    fontSize: 24,
    color: 'white',
    paddingLeft:20
  },

  modalText:{
    paddingTop:40,
    width:'100%',
    display:'flex',
  },
  flexIcon:{
    width:50,
    height:50,
    resizeMode: "cover",
  },

  imageContainer: {
    width: "48%",
    aspectRatio: 1,
    marginBottom: .1,
    borderWidth: 0.5,
    borderColor: "#ffff",
    borderRadius: 20,
    justifyContent: "center",
    alignItems: "center",
  
  },
  image: {
    width: "95%",
    resizeMode: "cover",
    borderRadius: 20,
  },

  imageText: {
    marginTop: 8,
    fontSize: 15,
    fontWeight: "bold",
    color: 'white',
    lineHeight: 20
  },

  innerContainer: {
    position: 'absolute',
    backgroundColor: 'rgba(0, 0, 0, 0.3)',
    width: '95%',
    borderRadius: 20, 
    paddingLeft:15,
    paddingTop: 8 
  },

  icon:{
    resizeMode: "contain",
    width: '18%'
  },

  subText: {
    fontSize: 12,
    marginTop: 12,
    color: "white",
  },
  mainHeading: {
    color: 'black',
    paddingTop: 40,
    paddingBottom: 15,
    paddingLeft: 30,
    fontSize: 16,
    color: '#4A682C'
  },

  iconsContainer:{
    flexDirection: "row",
    justifyContent: "space-around",
    alignItems: "center",
    paddingVertical: 25 ,
    paddingLeft : 60,
    marginHorizontal: 4,
    // marginLeft: 13,
  },

  iconContainer: {
    display : "flex",
    justifyContent: 'center',
    // alignItems: "flex-start",
    flexWrap : "nowrap",
    width: 100,
  }

});

export default ThirdPage;