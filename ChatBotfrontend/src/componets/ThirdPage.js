import React, {useState} from "react";
import { View, Text, TouchableOpacity, Image, StyleSheet, Modal, Button } from "react-native";
import {data} from './Data';
import TalkToMurimiButton from './Button'
import { SvgXml } from "react-native-svg";

const homeIcon = `../../assets/home.svg`;
const marketIcon = `../../assets/market.svg`;
const settingsIcon = `../../assets/settings.svg`;


const ThirdPage = () => {

  const handleImageClick = (text) => {
    setShowModal( !showModal);
    ;
  };

  const [showModal, setShowModal] = useState(null);

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
              onRequestClose={() => setShowModal(null)}
              visible={showModal}
            >
              <Text>{item.texttt}</Text>

              <Button
                title="Click To Close Modal"
                onPress={() => {
                  setShowModal(!showModal);
                }}
              />            
          </Modal>
        </TouchableOpacity>
      ))}
      <TalkToMurimiButton/>

      <View style={styles.iconsContainer} >
        <TouchableOpacity style={styles.iconContainer} >
        <Image source={require('../../assets/home.png')}/>
          <Text>Home</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.iconContainer}>
        <Image source={require('../../assets/market.png')}/>
          <Text style={styles.iconText}>Market</Text>
        </TouchableOpacity>
        <TouchableOpacity style={styles.iconContainer}>
        <Image source={require('../../assets/settings.png')}/>
          <Text style={styles.iconText}>Settings</Text>
        </TouchableOpacity>
      </View>
      <View style={styles.greenBorder} /> 
{/* 
        <Modal
          isOpen={i === showModal}
          animationType={'fade'}
          transparent={false}
          visible={showModal}
          onRequestClose={() => setShowModal(null)}>

          <View style={styles.modal}>
          {modalData.map((modalData, i) => (
           <View>
              <Text style={styles.text}>{modalData.text}</Text>
              <Button
                title="Click To Close Modal"
                onPress={() => {
                  setShowModal(!showModal);
                }}
              />
            </View>
      ))}      
          </View>
        </Modal> */}

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
    // paddingTop: 50,
    position: 'relative'
    
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
    alignItems: "flex-start",
    flexWrap : "nowrap",
    width: 100,
  }

});

export default ThirdPage;