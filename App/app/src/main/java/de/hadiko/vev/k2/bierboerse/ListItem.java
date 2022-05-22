package de.hadiko.vev.k2.bierboerse;

public class ListItem {
    private String name;
    private String currentPrice;

    public String getName() {
        return name;
    }

    public String getCurrentPrice() {
        return currentPrice;
    }

    public ListItem(String name, String currentPrice) {
        this.name = name;
        this.currentPrice = currentPrice;
    }

    public ListItem() {
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setCurrentPrice(String currentPrice) {
        this.currentPrice = currentPrice;
    }

    public class ListItem_Add extends ListItem {
        public ListItem_Add() {
            super();
        }
    }
}
