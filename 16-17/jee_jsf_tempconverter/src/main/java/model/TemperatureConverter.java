package model;

import java.io.Serializable;

/**
 *
 * @author Dominik
 */
public class TemperatureConverter implements Serializable{
    private static final long serialVersionUID = 1L;
    private double convert;
    private double converted;
    private boolean initial;
    private boolean error;
    private String unit;
    
    public double getConvert() {
        return convert;
    }
    
    public void setConvert(double convert) {
        this.convert = convert;
    }
    
    public double getConverted() {
        return converted;
    }
    
    public String getUnit() {
        return unit;
    }
    
    public boolean getInitial() {
        return initial;
    }

    public TemperatureConverter(){
        init();
    }

    public void init(){
        initial = true;
        error = false;
        converted = 0;
        convert = 0;
        unit="";
    }
    
    public String reset() {
        init();
        return "reset";
    }
    
    public void celsiusToFahrenheit() {
        if(convert < -273.15){
            error = true;
        } else {
            this.error = false;
            this.initial = false;
            this.unit = "Fahrenheit";
            this.converted = (convert * 1.8) + 32;
        }
    }
    
    public void celsiusToKelvin(){
        if(convert < -273.15){
            error = true;
        } else {
            this.error = false;
            this.initial = false;
            this.unit = "Kelvin";
            this.converted = convert + 273.15;
        }
    }
    
    public void fahrenheitToCelsius() {
        if(convert < -459.67){
            error = true;
        } else {
            this.error = false;
            this.initial = false;
            this.unit = "Celsius";
            this.converted = (convert - 32) / 1.8;
        }
    }
    
    public void fahrenheitToKelvin(){
        if(convert < -459.67){
            error = true;
        } else {
            this.error = false;
            this.initial = false;
            this.unit = "Kelvin";
            this.converted = ((convert - 32) / 1.8) + 273.15;
        }
    }
    
    public void kelvinToCelsius(){
        if(convert < 0){
            error = true;
        } else {
            this.error = false;
            this.initial = false;
            this.unit = "Celsius";
            this.converted = convert - 273.15;
        }
    }
    
    public void kelvinToFahrenheit(){
        if(convert < 0){
            error = true;
        } else {
            this.error = false;
            this.initial = false;
            this.unit = "Fahrenheit";
            this.converted = convert * 9 / 5 - 458.67;
        }
    }
}
